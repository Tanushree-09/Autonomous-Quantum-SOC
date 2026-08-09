from fastapi import FastAPI
from agents.detection_agent import DetectionAgent
from agents.threat_graph_agent import ThreatGraphAgent
from agents.threat_analysis_agent import ThreatAnalysisAgent
from agents.llm_agent import LLMAgent
from agents.ml_agent import MLAgent
from agents.quantum_risk_agent import QuantumRiskAgent
from agents.recommendation_agent import RecommendationAgent


ml_agent = MLAgent()

ml_agent.load_model(
    "models/ml_model.joblib"
)
llm_agent = LLMAgent()
recommendation_agent = RecommendationAgent()
quantum_agent = QuantumRiskAgent()
analysis_agent = ThreatAnalysisAgent()
graph_agent = ThreatGraphAgent()
detection_agent = DetectionAgent()

app = FastAPI(
    title="AQ-SOC",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "AQ-SOC Running"
    }


@app.get("/logs")
def logs():
    return {
        "message": "Logs are stored in Elasticsearch."
    }


@app.get("/detect/{attack_name}")
def detect_attack(attack_name: str):

    # ======================================
    # 1. Elasticsearch Detection
    # ======================================

    report = detection_agent.detect_attack(
        attack_name
    )


    # ======================================
    # 2. Threat Analysis
    # ======================================

    threat_analysis = analysis_agent.analyze(
        report
    )


    # ======================================
    # 3. ML Analysis
    # ======================================

    ml_result = ml_agent.analyze_attack(
        attack_name,
        sample_size=100
    )


    # ======================================
    # 4. Initial Threat Context
    # ======================================

    threat_context = {

        "statistics": report,

        "threat_analysis": threat_analysis,

        "ml_analysis": ml_result
    }


    # ======================================
    # 5. LLM Security Reasoning
    # ======================================

    llm_analysis = llm_agent.analyze_threat(
        threat_context
    )


    # ======================================
    # 6. Quantum Risk Analysis
    # ======================================

    quantum_result = quantum_agent.assess_risk(
        threat_context
    )


    # ======================================
    # 7. Add Quantum Evidence
    # ======================================

    threat_context["quantum_analysis"] = (
        quantum_result
    )


    # ======================================
    # 8. Recommendation
    # ======================================

    recommendation = (
        recommendation_agent.generate_recommendation(
            threat_context
        )
    )


    # ======================================
    # 9. Store Threat in Neo4j
    # ======================================

    graph_agent.create_graph(
        report
    )


    # ======================================
    # 10. Final AQ-SOC Response
    # ======================================

    return {

        "statistics":
            report,

        "threat_analysis":
            threat_analysis,

        "ml_analysis":
            ml_result,

        "llm_analysis":
            llm_analysis,

        "quantum_analysis":
            quantum_result,

        "recommendation":
            recommendation
    }