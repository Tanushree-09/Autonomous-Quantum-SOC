from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


class QuantumRiskAgent:

    def __init__(self):

        self.simulator = AerSimulator()


    def assess_risk(self, threat_context):

        statistics = threat_context["statistics"]
        ml_analysis = threat_context["ml_analysis"]

        attack = statistics["attack"]
        risk_score = threat_context.get(
            "threat_analysis",
            {}
        ).get("risk_score", 0)

        ml_confidence = ml_analysis[
            "average_confidence"
        ]

        print(
            "\n========== QUANTUM RISK ANALYSIS =========="
        )

        print(
            f"Attack: {attack}"
        )

        print(
            f"Risk score: {risk_score}"
        )

        print(
            f"ML confidence: {ml_confidence}"
        )


        # --------------------------------------
        # Quantum simulation
        # --------------------------------------

        circuit = QuantumCircuit(2, 2)

        # Create superposition
        circuit.h(0)

        # Entangle qubits
        circuit.cx(0, 1)

        # Measure
        circuit.measure(
            [0, 1],
            [0, 1]
        )


        job = self.simulator.run(
            circuit,
            shots=1024
        )

        result = job.result()

        counts = result.get_counts(
            circuit
        )


        # --------------------------------------
        # Quantum simulation metrics
        # --------------------------------------

        total_shots = sum(
            counts.values()
        )

        dominant_state = max(
            counts,
            key=counts.get
        )

        dominant_probability = (
            counts[dominant_state]
            / total_shots
        )


        # --------------------------------------
        # Quantum relevance
        # --------------------------------------

        if risk_score >= 70:

            quantum_relevance = "HIGH"

        elif risk_score >= 40:

            quantum_relevance = "MEDIUM"

        else:

            quantum_relevance = "LOW"


        # --------------------------------------
        # Final result
        # --------------------------------------

        return {

            "attack":
                attack,

            "quantum_relevance":
                quantum_relevance,

            "risk_score":
                risk_score,

            "ml_confidence":
                float(ml_confidence),

            "simulation": {

                "shots":
                    total_shots,

                "measurement_counts":
                    counts,

                "dominant_state":
                    dominant_state,

                "dominant_probability":
                    float(
                        dominant_probability
                    )
            },

            "quantum_assessment":
                "Quantum simulation completed."
        }