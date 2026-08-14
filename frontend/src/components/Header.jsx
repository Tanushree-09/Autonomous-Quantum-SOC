const Header = () => {
  return (
    <header className="border-b border-slate-800 bg-slate-950 px-6 py-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-wide text-white">
            AQ-SOC
          </h1>

          <p className="text-sm text-slate-400">
            Autonomous Quantum Security Operations Center
          </p>
        </div>

        <div className="flex items-center gap-2">
          <span className="h-2.5 w-2.5 rounded-full bg-emerald-400"></span>

          <span className="text-sm font-medium text-emerald-400">
            SYSTEM OPERATIONAL
          </span>
        </div>
      </div>
    </header>
  );
};

export default Header;