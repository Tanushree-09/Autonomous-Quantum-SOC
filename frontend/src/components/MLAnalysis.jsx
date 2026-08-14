const MLAnalysis = ({ analysis }) => {
  if (!analysis) return null;

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-lg font-semibold text-white">
        ML Analysis
      </h2>

      <p className="mb-5 text-sm text-slate-400">
        Machine-learning threat classification
      </p>

      <div className="space-y-4">
        <Metric
          label="Prediction"
          value={analysis.predicted_attack}
        />

        <Metric
          label="Confidence"
          value={`${(
            analysis.average_confidence * 100
          ).toFixed(2)}%`}
        />

        <Metric
          label="Prediction Accuracy"
          value={`${(
            analysis.prediction_accuracy * 100
          ).toFixed(0)}%`}
        />

        <Metric
          label="Samples Analyzed"
          value={analysis.samples_analyzed}
        />
      </div>
    </div>
  );
};

const Metric = ({ label, value }) => (
  <div className="flex items-center justify-between border-b border-slate-800 pb-3">
    <span className="text-sm text-slate-400">
      {label}
    </span>

    <span className="font-semibold text-white">
      {value ?? "—"}
    </span>
  </div>
);

export default MLAnalysis;