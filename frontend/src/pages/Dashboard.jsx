import { useState } from "react";

import Header from "../components/Header";
import RiskCard from "../components/RiskCard";
import AgentPipeline from "../components/AgentPipeline";
import NetworkStats from "../components/NetworkStats";
import MLAnalysis from "../components/MLAnalysis";
import QuantumRisk from "../components/QuantumRisk";
import SelfHealing from "../components/SelfHealing";
import RiskGauge from "../components/RiskGauge";
import NetworkChart from "../components/NetworkChart";
import QuantumChart from "../components/QuantumChart";

import { analyzeAttack } from "../services/api";

const Dashboard = () => {
  const [attack, setAttack] = useState("PortScan");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    try {
      setLoading(true);
      setError("");

      const result = await analyzeAttack(attack);

      setData(result);
    } catch (err) {
      console.error(err);
      setError(
        "Unable to connect to AQ-SOC backend."
      );
    } finally {
      setLoading(false);
    }
  };

  const threat = data?.threat_analysis;
  const quantum = data?.quantum_analysis;
  const attackTypes = [
  "BENIGN",
  "PortScan",
  "DoS Hulk",
  "DDoS",
  "DoS GoldenEye",
  "FTP-Patator",
  "SSH-Patator",
  "DoS slowloris",
  "DoS Slowhttptest",
  "Bot",
  "Web Attack ï¿½ Brute Force",
  "Web Attack ï¿½ XSS",
  "Infiltration",
  "Web Attack ï¿½ Sql Injection",
  "Heartbleed",
    ];  

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Header />

      <main className="mx-auto max-w-7xl space-y-6 p-6">

        {/* Attack Input */}
        <section className="rounded-xl border border-slate-800 bg-slate-900 p-5">
          <div className="flex flex-col gap-4 sm:flex-row">
            <div className="flex-1">
              <label className="mb-2 block text-sm text-slate-400">
                Attack Type
              </label>

              <select
                value={attack}
                onChange={(e) => setAttack(e.target.value)}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-4 py-3 text-white outline-none focus:border-slate-500"
              >
                {attackTypes.map((type) => (
                  <option key={type} value={type}>
                    {type}
                  </option>
                ))}
              </select>
            </div>

            <div className="flex items-end">
              <button
                onClick={handleAnalyze}
                disabled={loading}
                className="rounded-lg bg-white px-6 py-3 font-semibold text-slate-950 transition hover:bg-slate-200 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {loading
                  ? "Analyzing..."
                  : "Analyze Attack"}
              </button>
            </div>
          </div>

          {error && (
            <p className="mt-3 text-sm text-red-400">
              {error}
            </p>
          )}
        </section>

        {data && (
          <>
            {/* Top Risk Cards */}
            <section className="grid gap-4 md:grid-cols-4">
              <RiskCard
                title="Attack"
                value={data.attack_name}
                subtitle="Detected threat"
              />

              <RiskCard
                title="Severity"
                value={threat?.severity}
                subtitle="Threat classification"
                valueClass="text-red-400"
              />

              <RiskCard
                title="Risk Score"
                value={`${threat?.risk_score}/100`}
                subtitle="Calculated threat risk"
                valueClass="text-amber-400"
              />

              <RiskCard
                title="Quantum Relevance"
                value={quantum?.quantum_relevance}
                subtitle="Post-quantum exposure"
                valueClass="text-purple-400"
              />
            </section>

            {/* Risk + Agent Pipeline */}
            <section className="grid gap-6 lg:grid-cols-2">
            <RiskGauge
                score={threat?.risk_score}
                severity={threat?.severity}
            />

            <AgentPipeline />
            </section>

            {/* Network Analysis */}
            <section className="grid gap-6 lg:grid-cols-2">
            <NetworkStats
                statistics={data.statistics}
            />

            <MLAnalysis
                analysis={data.ml_analysis}
            />
            </section>

            {/* Quantum Analysis */}
            <section className="grid gap-6 lg:grid-cols-2">
            <QuantumRisk
                analysis={data.quantum_analysis}
            />

            <QuantumChart
                simulation={data.quantum_analysis?.simulation}
            />
            </section>

            {/* Network Visualization */}
            <NetworkChart
            statistics={data.statistics}
            />

            {/* Self-Healing */}
            {data.healing_result && (
            <SelfHealing
                healing={data.healing_result}
            />
            )}

            {/* Recommendation */}
            {data.recommendation && (
              <section className="rounded-xl border border-slate-800 bg-slate-900 p-6">
                <h2 className="text-lg font-semibold text-white">
                  Security Recommendation
                </h2>

                <div className="mt-5">
                  <p className="text-sm font-semibold text-slate-300">
                    Immediate Actions
                  </p>

                  <ul className="mt-3 space-y-2">
                    {data.recommendation.immediate_actions?.map(
                      (action, index) => (
                        <li
                          key={index}
                          className="rounded-lg bg-slate-950 p-3 text-sm text-slate-300"
                        >
                          {action}
                        </li>
                      )
                    )}
                  </ul>
                </div>

                <div className="mt-6 rounded-lg border border-purple-500/20 bg-purple-500/5 p-4">
                  <p className="text-sm font-semibold text-purple-400">
                    Post-Quantum Cryptography
                  </p>

                  <p className="mt-2 text-sm text-slate-300">
                    {
                      data.recommendation
                        .pqc_recommendation
                        ?.recommended_action
                    }
                  </p>
                </div>
              </section>
            )}

            {/* LLM Reasoning */}
            {data.llm_analysis && (
              <section className="rounded-xl border border-slate-800 bg-slate-900 p-6">
                <h2 className="text-lg font-semibold text-white">
                  LLM Security Reasoning
                </h2>

                <div className="mt-4 whitespace-pre-wrap text-sm leading-7 text-slate-300">
                  {data.llm_analysis}
                </div>
              </section>
            )}
          </>
        )}
      </main>
    </div>
  );
};

export default Dashboard;