const QuantumRisk = ({ analysis }) => {
  if (!analysis) return null;

  const simulation = analysis.simulation;

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-lg font-semibold text-white">
        Quantum Risk Analysis
      </h2>

      <p className="mb-5 text-sm text-slate-400">
        Qiskit quantum-risk simulation
      </p>

      <div className="grid grid-cols-2 gap-4">
        <Metric
          label="Quantum Relevance"
          value={analysis.quantum_relevance}
          highlight
        />

        <Metric
          label="Risk Score"
          value={`${analysis.risk_score}/100`}
        />

        <Metric
          label="Simulation Shots"
          value={simulation?.shots}
        />

        <Metric
          label="Dominant State"
          value={simulation?.dominant_state}
        />

        <Metric
          label="Dominant Probability"
          value={
            simulation
              ? `${(
                  simulation.dominant_probability * 100
                ).toFixed(2)}%`
              : "—"
          }
        />
      </div>

      {simulation?.measurement_counts && (
        <div className="mt-5">
          <p className="mb-2 text-xs uppercase tracking-wider text-slate-500">
            Measurement Counts
          </p>

          <div className="flex gap-3">
            {Object.entries(
              simulation.measurement_counts
            ).map(([state, count]) => (
              <div
                key={state}
                className="rounded-lg bg-slate-950 px-4 py-3"
              >
                <p className="text-xs text-slate-500">
                  State {state}
                </p>

                <p className="text-lg font-semibold text-white">
                  {count}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

const Metric = ({
  label,
  value,
  highlight = false,
}) => (
  <div className="rounded-lg bg-slate-950 p-4">
    <p className="text-xs text-slate-500">
      {label}
    </p>

    <p
      className={`mt-1 text-lg font-semibold ${
        highlight
          ? "text-purple-400"
          : "text-white"
      }`}
    >
      {value ?? "—"}
    </p>
  </div>
);

export default QuantumRisk;