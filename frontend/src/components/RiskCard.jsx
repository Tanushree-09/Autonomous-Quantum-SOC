const RiskCard = ({
  title,
  value,
  subtitle,
  valueClass = "text-white",
}) => {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
        {title}
      </p>

      <p className={`mt-3 text-3xl font-bold ${valueClass}`}>
        {value}
      </p>

      {subtitle && (
        <p className="mt-1 text-sm text-slate-400">
          {subtitle}
        </p>
      )}
    </div>
  );
};

export default RiskCard;