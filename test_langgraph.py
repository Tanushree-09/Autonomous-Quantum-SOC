from agents.detection_agent import DetectionAgent
from agents.threat_analysis_agent import ThreatAnalysisAgent
from agents.ml_agent import MLAgent
from agents.llm_agent import LLMAgent
from agents.quantum_risk_agent import QuantumRiskAgent
from agents.recommendation_agent import RecommendationAgent

from agents.soc_graph import SOCGraph


# ==========================================
# Initialize agents
# ==========================================

detection_agent = DetectionAgent()

threat_analysis_agent = ThreatAnalysisAgent()

ml_agent = MLAgent()

ml_agent.load_model(
    "models/ml_model.joblib"
)

llm_agent = LLMAgent()

quantum_agent = QuantumRiskAgent()

recommendation_agent = RecommendationAgent()


# ==========================================
# Build LangGraph
# ==========================================

soc = SOCGraph(

    detection_agent=detection_agent,

    threat_analysis_agent=
        threat_analysis_agent,

    ml_agent=
        ml_agent,

    llm_agent=
        llm_agent,

    quantum_agent=
        quantum_agent,

    recommendation_agent=
        recommendation_agent
)


# ==========================================
# Run
# ==========================================

result = soc.run(
    "PortScan"
)


# ==========================================
# Display result
# ==========================================

print("\n\n========== FINAL LANGGRAPH RESULT ==========")

print(
    "Attack:",
    result.get("attack_name")
)

print(
    "\nStatistics:"
)

print(
    result.get("statistics")
)

print(
    "\nThreat Analysis:"
)

print(
    result.get("threat_analysis")
)

print(
    "\nML Analysis:"
)

print(
    result.get("ml_analysis")
)

print(
    "\nQuantum Analysis:"
)

print(
    result.get("quantum_analysis")
)

print(
    "\nRecommendation:"
)

print(
    result.get("recommendation")
)

print(
    "\nStatus:",
    result.get("status")
)