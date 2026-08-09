# Autonomous Quantum Security Operations Center (AQ-SOC)

An autonomous cybersecurity operations platform that combines AI-driven threat detection, machine learning, LLM-based security reasoning, quantum-risk analysis, and graph-based threat intelligence.

## Current Architecture

CICIDS2017
        ↓
Elasticsearch
        ↓
Detection Agent
        ↓
Threat Analysis Agent
        ↓
ML Agent
        ↓
LLM Agent
        ↓
Quantum Risk Agent
        ↓
Recommendation Agent
        ↓
Neo4j

## Technologies

- Python
- FastAPI
- Elasticsearch
- Neo4j
- Scikit-learn
- Random Forest
- LLM APIs
- Qiskit Aer
- Docker

## Current Capabilities

- Network attack detection using Elasticsearch
- Threat statistics extraction
- ML-based attack classification
- LLM-based threat analysis
- Quantum-risk simulation
- Security recommendations
- Threat relationship storage in Neo4j

## Dataset

The system currently uses the CICIDS2017 cybersecurity dataset.

The dataset itself is not included in this repository because of its size.

## Project Status

### Completed

- [x] Elasticsearch integration
- [x] Neo4j integration
- [x] Detection Agent
- [x] Threat Analysis Agent
- [x] ML Agent
- [x] LLM Agent
- [x] Quantum Risk Agent
- [x] Recommendation Agent
- [x] FastAPI backend

### Planned

- [ ] Grafana monitoring dashboard
- [ ] LangGraph orchestration
- [ ] Self-healing response agent
- [ ] React frontend
- [ ] Backend/frontend integration