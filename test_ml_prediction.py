from agents.ml_agent import MLAgent


agent = MLAgent()


# Load the already trained model
agent.load_model()


# Get a real flow directly from Elasticsearch
flow = agent.get_flow_from_elasticsearch()


print("\n========== REAL FLOW ==========")

print(flow)


# Predict the attack
result = agent.predict(flow)


print("\n========== ML PREDICTION ==========")

print(result)