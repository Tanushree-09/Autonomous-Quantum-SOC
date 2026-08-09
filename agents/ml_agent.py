import pandas as pd
import numpy as np
import joblib

from elasticsearch import Elasticsearch, helpers

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report


class MLAgent:

    def __init__(self):

        self.es = Elasticsearch(
            "http://localhost:9200"
        )

        self.INDEX_NAME = "network_logs"

        self.model = None

        self.label_encoder = LabelEncoder()

        self.feature_columns = None


    def load_training_data(self, samples_per_class=5000):

        print("Fetching balanced training data from Elasticsearch...")

        # Get all available labels and their counts
        response = self.es.search(
            index=self.INDEX_NAME,
            size=0,
            aggs={
                "attack_types": {
                    "terms": {
                        "field": "Label.keyword",
                        "size": 100
                    }
                }
            }
        )

        buckets = response["aggregations"]["attack_types"]["buckets"]

        records = []

        print("\nSampling:")

        for bucket in buckets:

            label = bucket["key"]
            available = bucket["doc_count"]

            sample_size = min(
                samples_per_class,
                available
            )

            print(
                f"{label:<30} "
                f"{available:>10} available -> "
                f"{sample_size:>6} sampled"
            )

            query = {
                "query": {
                    "term": {
                        "Label.keyword": label
                    }
                }
            }

            count = 0

            for hit in helpers.scan(
                self.es,
                index=self.INDEX_NAME,
                query=query,
                size=1000
            ):

                records.append(
                    hit["_source"]
                )

                count += 1

                if count >= sample_size:
                    break


        if not records:

            raise ValueError(
                "No training data found in Elasticsearch."
            )


        df = pd.DataFrame(records)

        print(
            f"\nTotal training records loaded: {len(df)}"
        )

        print("\nTraining distribution:")

        print(
            df["Label"].value_counts()
        )

        return df


    def prepare_data(self, df):

        if "Label" not in df.columns:

            raise ValueError(
                "Label field not found."
            )


        # Separate features and target

        X = df.drop(
            columns=["Label"]
        )

        y = df["Label"]


        # Convert feature values to numeric

        X = X.apply(
            pd.to_numeric,
            errors="coerce"
        )


        # Handle infinity

        X = X.replace(
            [np.inf, -np.inf],
            np.nan
        )


        # Handle missing values

        X = X.fillna(0)


        # Encode attack labels

        y = self.label_encoder.fit_transform(
            y
        )


        self.feature_columns = X.columns.tolist()


        return X, y


    def train(self, samples_per_class=5000):

        df = self.load_training_data(
            samples_per_class
        )


        X, y = self.prepare_data(
            df
        )


        print(
            f"Features: {len(self.feature_columns)}"
        )

        print(
            f"Classes: {self.label_encoder.classes_.tolist()}"
        )


        X_train, X_test, y_train, y_test = train_test_split(

            X,
            y,

            test_size=0.2,

            random_state=42,

            stratify=y
        )


        print("Training ML model...")


        self.model = RandomForestClassifier(

            n_estimators=200,

            random_state=42,

            n_jobs=-1,

            class_weight="balanced"
        )


        self.model.fit(
            X_train,
            y_train
        )


        predictions = self.model.predict(
            X_test
        )


        accuracy = accuracy_score(
            y_test,
            predictions
        )


        print(
            f"\nAccuracy: {accuracy:.4f}"
        )


        print("\nClassification Report:")

        print(
            classification_report(

                y_test,

                predictions,

                target_names=self.label_encoder.classes_,

                zero_division=0
            )
        )


        return {
            "accuracy": float(accuracy),

            "classes":
                self.label_encoder.classes_.tolist(),

            "training_samples":
                len(X_train),

            "testing_samples":
                len(X_test)
        }


    def predict(self, flow):

        if self.model is None:

            raise RuntimeError(
                "ML model has not been trained."
            )


        df = pd.DataFrame(
            [flow]
        )


        # Ensure exactly the same
        # features used during training

        df = df.reindex(
            columns=self.feature_columns,
            fill_value=0
        )


        df = df.apply(
            pd.to_numeric,
            errors="coerce"
        )


        df = df.replace(
            [np.inf, -np.inf],
            np.nan
        )


        df = df.fillna(0)


        prediction = self.model.predict(
            df
        )[0]


        probabilities = self.model.predict_proba(
            df
        )[0]


        attack_name = self.label_encoder.inverse_transform(
            [prediction]
        )[0]


        confidence = float(
            max(probabilities)
        )


        return {

            "predicted_attack":
                attack_name,

            "confidence":
                confidence
        }
    
    def save_model(self, path="models/ml_model.joblib"):

        if self.model is None:
            raise RuntimeError(
                "Model has not been trained."
            )

        model_data = {
            "model": self.model,
            "label_encoder": self.label_encoder,
            "feature_columns": self.feature_columns
        }

        joblib.dump(
            model_data,
            path
        )

        print(
            f"ML model saved to {path}"
        )


    def load_model(self, path="models/ml_model.joblib"):

        model_data = joblib.load(
            path
        )

        self.model = model_data["model"]

        self.label_encoder = model_data[
            "label_encoder"
        ]

        self.feature_columns = model_data[
            "feature_columns"
        ]

        print(
            f"ML model loaded from {path}"
        )
    def get_flow_from_elasticsearch(self):

        response = self.es.search(
            index=self.INDEX_NAME,
            size=1,
            query={
                "exists": {
                    "field": "Label"
                }
            }
        )

        hits = response["hits"]["hits"]

        if not hits:
            raise ValueError(
                "No network flows found in Elasticsearch."
            )

        return hits[0]["_source"]
    def get_attack_flow(self, attack_name):

        response = self.es.search(
            index=self.INDEX_NAME,
            size=1,
            query={
                "match": {
                    "Label": attack_name
                }
            }
        )

        hits = response["hits"]["hits"]

        if not hits:
            raise ValueError(
                f"No records found for attack: {attack_name}"
            )

        return hits[0]["_source"]
    def analyze_attack(self, attack_name, sample_size=100):
        """
        Fetch real flows for an attack from Elasticsearch
        and run the trained ML model on them.
        """

        if self.model is None:
            raise RuntimeError(
                "ML model has not been loaded."
            )

        query = {
            "query": {
                "term": {
                    "Label.keyword": attack_name
                }
            }
        }

        predictions = []
        confidences = []

        print(
            f"Fetching real {attack_name} flows "
            f"from Elasticsearch..."
        )

        count = 0

        for hit in helpers.scan(
            self.es,
            index=self.INDEX_NAME,
            query=query,
            size=1000
        ):

            flow = hit["_source"]

            result = self.predict(flow)

            predictions.append(
                result["predicted_attack"]
            )

            confidences.append(
                result["confidence"]
            )

            count += 1

            if count >= sample_size:
                break

        if not predictions:
            raise ValueError(
                f"No flows found for attack: {attack_name}"
            )

        prediction_counts = {}

        for prediction in predictions:

            prediction_counts[prediction] = (
                prediction_counts.get(prediction, 0) + 1
            )

        majority_prediction = max(
            prediction_counts,
            key=prediction_counts.get
        )

        average_confidence = (
            sum(confidences) / len(confidences)
        )

        correct_predictions = sum(
            1
            for prediction in predictions
            if prediction == attack_name
        )

        prediction_accuracy = (
            correct_predictions / len(predictions)
        )

        return {
            "actual_attack": attack_name,

            "samples_analyzed": len(predictions),

            "predicted_attack": majority_prediction,

            "prediction_accuracy":
                float(prediction_accuracy),

            "average_confidence":
                float(average_confidence),

            "prediction_distribution":
                prediction_counts
        }