const RiskGauge = ({ score = 0, severity = "UNKNOWN" }) => {
  const percentage = Math.min(Math.max(score, 0), 100);

  const getColor = () => {
    if (percentage >= 80) return "bg-red-500";
    if (percentage >= 60) return "bg-orange-500";
    if (percentage >= 40) return "bg-yellow-500";
    return "bg-emerald-500";
  };

  const getTextColor = () => {
    if (percentage >= 80) return "text-red-400";
    if (percentage >= 60) return "text-orange-400";
    if (percentage >= 40) return "text-yellow-400";
    return "text-emerald-400";
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-lg font-semibold text-white">
            Threat Risk
          </h2>

          <p className="text-sm text-slate-400">
            Autonomous risk assessment
          </p>
        </div>

        <span
          className={`rounded-full bg-slate-950 px-3 py-1 text-xs font-bold ${getTextColor()}`}
        >
          {severity}
        </span>
      </div>

      <div className="mt-6 flex items-center gap-6">
        {/* Score */}
        <div className="flex h-28 w-28 shrink-0 flex-col items-center justify-center rounded-full border-8 border-slate-800">
          <span
            className={`text-3xl font-bold ${getTextColor()}`}
          >
            {percentage}
          </span>

          <span className="text-xs text-slate-500">
            / 100
          </span>
        </div>

        {/* Progress */}
        <div className="flex-1">
          <div className="mb-2 flex justify-between">
            <span className="text-xs text-slate-500">
              Risk level
            </span>

            <span className={`text-xs font-semibold ${getTextColor()}`}>
              {percentage}%
            </span>
          </div>

          <div className="h-3 overflow-hidden rounded-full bg-slate-800">
            <div
              className={`h-full rounded-full transition-all duration-700 ${getColor()}`}
              style={{
                width: `${percentage}%`,
              }}
            />
          </div>

          <div className="mt-3 flex justify-between text-[10px] text-slate-600">
            <span>LOW</span>
            <span>MEDIUM</span>
            <span>HIGH</span>
            <span>CRITICAL</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RiskGauge;