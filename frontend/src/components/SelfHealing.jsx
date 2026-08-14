const SelfHealing = ({ healing }) => {
  if (!healing) return null;

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-lg font-semibold text-white">
            Self-Healing
          </h2>

          <p className="text-sm text-slate-400">
            Autonomous remediation workflow
          </p>
        </div>

        <span className="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-semibold text-emerald-400">
          {healing.self_healing_status}
        </span>
      </div>

      <div className="mt-5 space-y-3">
        {healing.actions?.map((item, index) => (
          <div
            key={index}
            className="rounded-lg border border-slate-800 bg-slate-950 p-4"
          >
            <div className="flex items-center justify-between">
              <span className="font-medium text-white">
                {item.action}
              </span>

              <span className="text-xs font-semibold text-emerald-400">
                {item.status}
              </span>
            </div>

            <p className="mt-1 text-sm text-slate-500">
              Target: {item.target}
            </p>
          </div>
        ))}
      </div>

      {healing.verification && (
        <div className="mt-4 rounded-lg bg-emerald-500/5 p-4">
          <p className="text-sm font-medium text-emerald-400">
            ✓ {healing.verification.message}
          </p>

          <p className="mt-1 text-xs text-slate-500">
            Actions verified:{" "}
            {healing.verification.actions_verified}
          </p>
        </div>
      )}
    </div>
  );
};

export default SelfHealing;