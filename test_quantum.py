from agents.quantum_risk_agent import QuantumRiskAgent


agent = QuantumRiskAgent()


threat_context = {

    "statistics": {

        "attack": "PortScan"

    },

    "ml_analysis": {

        "average_confidence": 0.99405

    },

    "threat_analysis": {

        "risk_score": 70

    }

}


result = agent.assess_risk(
    threat_context
)


print("\n========== RESULT ==========")

print(result)