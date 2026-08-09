class RecommendationAgent:

    def __init__(self):
        pass


    def generate_recommendation(self, threat_context):

        statistics = threat_context["statistics"]

        threat_analysis = threat_context[
            "threat_analysis"
        ]

        ml_analysis = threat_context[
            "ml_analysis"
        ]

        quantum_analysis = threat_context[
            "quantum_analysis"
        ]


        attack = statistics["attack"]

        severity = threat_analysis.get(
            "severity",
            "UNKNOWN"
        )

        risk_score = threat_analysis.get(
            "risk_score",
            0
        )

        ml_prediction = ml_analysis.get(
            "predicted_attack",
            "UNKNOWN"
        )

        ml_confidence = ml_analysis.get(
            "average_confidence",
            0
        )

        quantum_relevance = quantum_analysis.get(
            "quantum_relevance",
            "UNKNOWN"
        )


        # ==========================================
        # Immediate Security Actions
        # ==========================================

        immediate_actions = []


        if severity == "HIGH" or risk_score >= 70:

            immediate_actions.append(
                "Investigate the source of the detected attack."
            )

            immediate_actions.append(
                "Review exposed network services and "
                "unnecessary open ports."
            )

            immediate_actions.append(
                "Inspect security logs for follow-up "
                "exploitation attempts."
            )


        if attack == "PortScan":

            immediate_actions.append(
                "Restrict unnecessary externally exposed ports."
            )

            immediate_actions.append(
                "Review firewall rules and network "
                "segmentation."
            )


        # ==========================================
        # ML Validation
        # ==========================================

        if (
            ml_prediction == attack
            and ml_confidence >= 0.80
        ):

            detection_confidence = "HIGH"

        elif ml_prediction == attack:

            detection_confidence = "MEDIUM"

        else:

            detection_confidence = "LOW"


        # ==========================================
        # PQC Recommendation
        # ==========================================

        pqc_recommendation = {

            "required": False,

            "priority": "NORMAL",

            "reason":
                "The detected network activity is not "
                "itself evidence of a quantum attack.",

            "recommended_action":
                "Inventory cryptographic algorithms "
                "used by affected systems and identify "
                "RSA/ECC dependencies for future PQC migration."
        }


        # ==========================================
        # Quantum relevance
        # ==========================================

        if quantum_relevance == "HIGH":

            pqc_recommendation["priority"] = "HIGH"

            pqc_recommendation["reason"] = (
                "The threat has high conventional risk "
                "and warrants assessment of cryptographic "
                "dependencies and future quantum exposure."
            )

            pqc_recommendation["required"] = True


        elif quantum_relevance == "MEDIUM":

            pqc_recommendation["priority"] = "MEDIUM"

            pqc_recommendation["reason"] = (
                "The threat warrants a review of "
                "cryptographic dependencies and "
                "future quantum exposure."
            )


        # ==========================================
        # Final Recommendation
        # ==========================================

        return {

            "attack":
                attack,

            "severity":
                severity,

            "risk_score":
                risk_score,

            "detection_confidence":
                detection_confidence,

            "ml_prediction":
                ml_prediction,

            "ml_confidence":
                float(ml_confidence),

            "quantum_relevance":
                quantum_relevance,

            "immediate_actions":
                immediate_actions,

            "pqc_recommendation":
                pqc_recommendation
        }