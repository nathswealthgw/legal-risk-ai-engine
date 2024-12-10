import { RiskCard } from "../components/RiskCard";
import { useRiskData } from "../hooks/useRiskData";

export function Dashboard() {
  const items = useRiskData();
  const criticalCount = items.filter((x) => x.category === "critical").length;

  return (
    <main className="container">
      <header>
        <h1>Legal Risk AI Engine</h1>
        <p>Critical Devices: {criticalCount}</p>
      </header>
      <section className="grid">
        {items.map((item) => (
          <RiskCard key={item.deviceId} item={item} />
        ))}
      </section>
    </main>
  );
}
