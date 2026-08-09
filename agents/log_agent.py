import os
import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch, helpers


class LogAgent:

    def __init__(self):
        self.es = Elasticsearch("http://localhost:9200")
        self.INDEX_NAME = "network_logs"

    def load_all_logs(self, folder_path):

        csv_files = [
            file
            for file in os.listdir(folder_path)
            if file.endswith(".csv")
        ]

        print(f"Found {len(csv_files)} dataset(s).\n")

        total_logs = 0

        for file in csv_files:

            try:
                print(f"Indexing {file}...")

                path = os.path.join(folder_path, file)

                logs = self.load_logs(path)

                print(f"Indexed {len(logs)} records.\n")

                total_logs += len(logs)

            except Exception as e:
                print(f"Failed to index {file}")
                print(e)
                print()

        print("=" * 50)
        print(f"Finished indexing {total_logs} logs.")
        print("=" * 50)

    def load_logs(self, path):

        df = pd.read_csv(path)

        # Remove duplicate columns
        df = df.loc[:, ~df.columns.duplicated()]

        # Replace '.' with '_'
        df.columns = [col.replace(".", "_") for col in df.columns]

        # Remove leading/trailing spaces
        df.columns = df.columns.str.strip()

        # Replace invalid values
        df.replace([np.inf, -np.inf], None, inplace=True)
        df = df.where(pd.notnull(df), None)

        logs = df.to_dict(orient="records")

        self.store_logs(logs)

        return logs

    def store_logs(self, logs):

        try:

            actions = [
                {
                    "_index": self.INDEX_NAME,
                    "_source": log
                }
                for log in logs
            ]

            success, errors = helpers.bulk(
                self.es,
                actions,
                raise_on_error=False
            )

            print("Indexed:", success)
            print("Failed :", len(errors))

            if errors:
                print("First Error:")
                print(errors[0])

        except Exception as e:
            print(e)