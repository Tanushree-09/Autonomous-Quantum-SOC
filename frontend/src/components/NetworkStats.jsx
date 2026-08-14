const NetworkStats = ({ statistics }) => {
  if (!statistics) return null;

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-lg font-semibold text-white">
        Network Statistics
      </h2>

      <p className="mb-5 text-sm text-slate-400">
        Elasticsearch-derived attack telemetry
      </p>

      <div className="grid grid-cols-2 gap-4">
        <Stat
          label="Total Events"
          value={statistics.total_events?.toLocaleString()}
        />

        <Stat
          label="Flow Duration"
          value={`${Math.round(
            statistics.average_flow_duration
          ).toLocaleString()} μs`}
        />

        <Stat
          label="Packets / Second"
          value={Math.round(
            statistics.average_packets_per_second
          ).toLocaleString()}
        />

        <Stat
          label="Bytes / Second"
          value={Math.round(
            statistics.average_bytes_per_second
          ).toLocaleString()}
        />
      </div>

      <div className="mt-5">
        <p className="mb-2 text-xs uppercase tracking-wider text-slate-500">
          Top Targeted Ports
        </p>

        <div className="flex flex-wrap gap-2">
          {statistics.top_ports?.map((port) => (
            <span
              key={port}
              className="rounded-md bg-slate-800 px-3 py-1 text-sm text-slate-300"
            >
              {port}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};

const Stat = ({ label, value }) => {
  return (
    <div className="rounded-lg bg-slate-950 p-4">
      <p className="text-xs text-slate-500">
        {label}
      </p>

      <p className="mt-1 text-lg font-semibold text-white">
        {value ?? "—"}
      </p>
    </div>
  );
};

export default NetworkStats;