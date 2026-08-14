import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const NetworkChart = ({ statistics }) => {
  if (!statistics) return null;

  const data = [
    {
      metric: "Packets/s",
      value: Math.round(
        statistics.average_packets_per_second || 0
      ),
    },
    {
      metric: "Bytes/s",
      value: Math.round(
        statistics.average_bytes_per_second || 0
      ),
    },
  ];

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <div className="mb-5">
        <h2 className="text-lg font-semibold text-white">
          Network Traffic Profile
        </h2>

        <p className="text-sm text-slate-400">
          Observed traffic characteristics
        </p>
      </div>

      <div className="h-72 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid
              strokeDasharray="3 3"
              stroke="#1e293b"
            />

            <XAxis
              dataKey="metric"
              stroke="#64748b"
            />

            <YAxis
              stroke="#64748b"
            />

            <Tooltip
              contentStyle={{
                backgroundColor: "#020617",
                border: "1px solid #334155",
                borderRadius: "8px",
                color: "#fff",
              }}
            />

            <Bar
              dataKey="value"
              fill="#38bdf8"
              radius={[6, 6, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default NetworkChart;