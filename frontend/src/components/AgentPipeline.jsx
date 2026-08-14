const AgentPipeline = ({ completed = true }) => {
  const agents = [
    "Detection",
    "Threat Analysis",
    "ML",
    "LLM",
    "Quantum Risk",
    "Recommendation",
    "Self-Healing",
  ];

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <div className="mb-5">
        <h2 className="text-lg font-semibold text-white">
          Agent Execution Pipeline
        </h2>

        <p className="text-sm text-slate-400">
          Autonomous LangGraph workflow
        </p>
      </div>

      <div className="flex flex-wrap items-center gap-3">
        {agents.map((agent, index) => (
          <div
            key={agent}
            className="flex items-center gap-3"
          >
            <div
              className={`rounded-lg border px-4 py-3 ${
                completed
                  ? "border-emerald-500/30 bg-emerald-500/10"
                  : "border-slate-700 bg-slate-800"
              }`}
            >
              <div className="flex items-center gap-2">
                <span
                  className={`h-2 w-2 rounded-full ${
                    completed
                      ? "bg-emerald-400"
                      : "bg-slate-500"
                  }`}
                />

                <span className="text-sm font-medium text-slate-200">
                  {agent}
                </span>
              </div>
            </div>

            {index < agents.length - 1 && (
              <span className="text-slate-600">
                →
              </span>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default AgentPipeline;