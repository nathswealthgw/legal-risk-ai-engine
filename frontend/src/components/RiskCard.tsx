import { RiskItem } from "../services/api";

export function RiskCard({ item }: { item: RiskItem }) {
  return (
    <article className={`risk-card ${item.category}`}>
      <h3>{item.deviceId}</h3>
      <p>Risk Score: {item.riskScore.toFixed(2)}</p>
      <p>Category: {item.category.toUpperCase()}</p>
      <p>Projected Downtime: {item.downtimeHours}h</p>
    </article>
  );
}
