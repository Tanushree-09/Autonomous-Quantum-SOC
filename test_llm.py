from agents.llm_agent import LLMAgent


agent = LLMAgent()


threat = {

    "attack": "PortScan",

    "total_events": 10000,

    "top_ports": [
        80,
        21,
        22,
        443
    ],

    "average_flow_duration":
        82820.22,

    "average_packets_per_second":
        62690.56,

    "average_bytes_per_second":
        220359.75,

    "ml_prediction": "PortScan",

    "ml_confidence": 0.445,

    "risk_score": 70,

    "severity": "HIGH"
}


analysis = agent.analyze_threat(
    threat
)


print("\n========== LLM THREAT ANALYSIS ==========\n")

print(analysis)