from agents.ml_agent import MLAgent


agent = MLAgent()

result = agent.train(
    samples_per_class=5000
)

agent.save_model()

print("\n========== ML RESULT ==========")

print(result)