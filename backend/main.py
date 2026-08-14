
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.detection_agent import DetectionAgent
from agents.threat_analysis_agent import ThreatAnalysisAgent
from agents.llm_agent import LLMAgent
from agents.ml_agent import MLAgent
from agents.quantum_risk_agent import QuantumRiskAgent
from agents.recommendation_agent import RecommendationAgent
from agents.soc_graph import SOCGraph


# ==========================================
# Initialize Agents
# ==========================================

ml_agent = MLAgent()

ml_agent.load_model(
    "models/ml_model.joblib"
)

llm_agent = LLMAgent()

recommendation_agent = RecommendationAgent()

quantum_agent = QuantumRiskAgent()

analysis_agent = ThreatAnalysisAgent()

detection_agent = DetectionAgent()


# ==========================================
# LangGraph
# ==========================================

soc_graph = SOCGraph(
    detection_agent=detection_agent,
    threat_analysis_agent=analysis_agent,
    ml_agent=ml_agent,
    llm_agent=llm_agent,
    quantum_agent=quantum_agent,
    recommendation_agent=recommendation_agent
)


# ==========================================
# FastAPI
# ==========================================

app = FastAPI(
    title="AQ-SOC",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


# ==========================================
# Main Analysis API
# ==========================================

@app.post("/api/analyze")
def analyze_attack(data: dict):

    attack = data.get("attack")

    if not attack:

        return {
            "error": "Attack name is required"
        }

    result = soc_graph.run(
        attack
    )

    return result