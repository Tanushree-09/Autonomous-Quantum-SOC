import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const QuantumChart = ({ simulation }) => {
  if (!simulation?.measurement_counts) {
    return null;
  }

  const data = Object.entries(
    simulation.measurement_counts
  ).map(([state, count]) => ({
    state,
    count,
  }));

  const COLORS = [
    "#a855f7",
    "#38bdf8",
    "#22c55e",
    "#f97316",
  ];

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <div className="mb-5">
        <h2 className="text-lg font-semibold text-white">
          Quantum Measurement Distribution
        </h2>

        <p className="text-sm text-slate-400">
          Qiskit Aer simulation results
        </p>
      </div>

      <div className="h-72 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={data}
              dataKey="count"
              nameKey="state"
              cx="50%"
              cy="50%"
              outerRadius={100}
              label
            >
              {data.map((_, index) => (
                <Cell
                  key={index}
                  fill={
                    COLORS[index % COLORS.length]
                  }
                />
              ))}
            </Pie>

            <Tooltip
              contentStyle={{
                backgroundColor: "#020617",
                border: "1px solid #334155",
                borderRadius: "8px",
                color: "#fff",
              }}
            />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default QuantumChart;