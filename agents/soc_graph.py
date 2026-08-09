from typing import TypedDict, Any

from langgraph.graph import StateGraph, START, END
from agents.self_healing_agent import SelfHealingAgent

class SOCState(TypedDict, total=False):

    # Input
    attack_name: str

    # Agent outputs
    statistics: dict
    threat_analysis: dict
    ml_analysis: dict
    llm_analysis: str
    quantum_analysis: dict
    recommendation: dict

    # Future self-healing
    healing_action: dict
    healing_result: dict

    status: str


class SOCGraph:

    def __init__(
        self,
        detection_agent,
        threat_analysis_agent,
        ml_agent,
        llm_agent,
        quantum_agent,
        recommendation_agent
    ):

        self.detection_agent = detection_agent
        self.threat_analysis_agent = threat_analysis_agent
        self.self_healing_agent = SelfHealingAgent()
        self.ml_agent = ml_agent
        self.llm_agent = llm_agent
        self.quantum_agent = quantum_agent
        self.recommendation_agent = recommendation_agent

        self.graph = self._build_graph()


    # ==========================================
    # 1. Detection Agent
    # ==========================================

    def detection_node(self, state: SOCState):

        print("\n========== LANGGRAPH ==========")
        print("Running Detection Agent...")

        attack = state["attack_name"]

        report = self.detection_agent.detect_attack(
            attack
        )

        return {
            "statistics": report
        }


    # ==========================================
    # 2. Threat Analysis Agent
    # ==========================================

    def threat_analysis_node(self, state: SOCState):

        print("Running Threat Analysis Agent...")

        analysis = self.threat_analysis_agent.analyze(
            state["statistics"]
        )

        return {
            "threat_analysis": analysis
        }


    # ==========================================
    # 3. ML Agent
    # ==========================================

    def ml_node(self, state: SOCState):

        print("Running ML Agent...")

        attack = state["attack_name"]

        result = self.ml_agent.analyze_attack(
            attack,
            sample_size=100
        )

        return {
            "ml_analysis": result
        }


    # ==========================================
    # 4. LLM Agent
    # ==========================================

    def llm_node(self, state: SOCState):

        print("Running LLM Agent...")

        threat_context = {

            "statistics":
                state["statistics"],

            "threat_analysis":
                state["threat_analysis"],

            "ml_analysis":
                state["ml_analysis"]
        }

        result = self.llm_agent.analyze_threat(
            threat_context
        )

        return {
            "llm_analysis": result
        }


    # ==========================================
    # 5. Quantum Risk Agent
    # ==========================================

    def quantum_node(self, state: SOCState):

        print("Running Quantum Risk Agent...")

        threat_context = {

            "statistics":
                state["statistics"],

            "threat_analysis":
                state["threat_analysis"],

            "ml_analysis":
                state["ml_analysis"]
        }

        result = self.quantum_agent.assess_risk(
            threat_context
        )

        return {
            "quantum_analysis": result
        }


    # ==========================================
    # 6. Recommendation Agent
    # ==========================================

    def recommendation_node(self, state: SOCState):

        print("Running Recommendation Agent...")

        threat_context = {

            "statistics":
                state["statistics"],

            "threat_analysis":
                state["threat_analysis"],

            "ml_analysis":
                state["ml_analysis"],

            "llm_analysis":
                state["llm_analysis"],

            "quantum_analysis":
                state["quantum_analysis"]
        }

        result = (
            self.recommendation_agent
            .generate_recommendation(
                threat_context
            )
        )

        return {
            "recommendation": result,
            "status": "analysis_complete"
        }

    # ==========================================
# 7. Self-Healing Agent
# ==========================================

    def self_healing_node(self, state: SOCState):

        print("Running Self-Healing Agent...")

        threat_context = {

            "statistics":
                state["statistics"],

            "threat_analysis":
                state["threat_analysis"],

            "ml_analysis":
                state["ml_analysis"],

            "llm_analysis":
                state["llm_analysis"],

            "quantum_analysis":
                state["quantum_analysis"],

            "recommendation":
                state["recommendation"]
        }

        result = self.self_healing_agent.heal(
            threat_context
        )

        return {
            "healing_result": result,
            "status": "self_healing_complete"
        }
    # ==========================================
    # Build LangGraph
    # ==========================================

    def _build_graph(self):

        builder = StateGraph(SOCState)


        builder.add_node(
            "detection",
            self.detection_node
        )

        builder.add_node(
            "threat_analysis",
            self.threat_analysis_node
        )

        builder.add_node(
            "ml",
            self.ml_node
        )

        builder.add_node(
            "llm",
            self.llm_node
        )

        builder.add_node(
            "quantum",
            self.quantum_node
        )

        builder.add_node(
            "recommendation",
            self.recommendation_node
        )

        builder.add_node(
            "self_healing",
            self.self_healing_node
        )


        # ======================================
        # Workflow
        # ======================================

        builder.add_edge(
            START,
            "detection"
        )

        builder.add_edge(
            "detection",
            "threat_analysis"
        )

        builder.add_edge(
            "threat_analysis",
            "ml"
        )

        builder.add_edge(
            "ml",
            "llm"
        )

        builder.add_edge(
            "llm",
            "quantum"
        )

        builder.add_edge(
            "quantum",
            "recommendation"
        )

        builder.add_edge(
            "recommendation",
            "self_healing"
        )

        builder.add_edge(
            "self_healing",
            END
        )


        return builder.compile()


    # ==========================================
    # Execute SOC
    # ==========================================

    def run(
        self,
        attack_name
    ):

        initial_state: SOCState = {

            "attack_name":
                attack_name,

            "status":
                "running"
        }

        result = self.graph.invoke(
            initial_state
        )

        return result