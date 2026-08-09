from agents.ml_agent import MLAgent


agent = MLAgent()


# Load the already trained model
agent.load_model()


# Get a REAL PortScan flow
flow = agent.get_attack_flow(
    "DDoS"
)


print("\n========== REAL ATTACK FLOW ==========")

print("Actual Label:")
print(flow["Label"])

print("\nDestination Port:")
print(flow["Destination Port"])

print("\nFlow Duration:")
print(flow["Flow Duration"])


# Remove the known answer before displaying prediction
actual_label = flow["Label"]


# ML prediction
prediction = agent.predict(flow)


print("\n========== ML PREDICTION ==========")

print(
    "Actual attack:",
    actual_label
)

print(
    "Predicted attack:",
    prediction["predicted_attack"]
)

print(
    "Confidence:",
    prediction["confidence"]
)


# Compare
if actual_label == prediction["predicted_attack"]:

    print("\nRESULT: CORRECT PREDICTION")

else:

    print("\nRESULT: INCORRECT PREDICTION")