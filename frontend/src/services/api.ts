export type RiskItem = {
  deviceId: string;
  riskScore: number;
  category: "low" | "medium" | "high" | "critical";
  downtimeHours: number;
};

export async function fetchRiskData(): Promise<RiskItem[]> {
  return [
    { deviceId: "dev-1001", riskScore: 0.91, category: "critical", downtimeHours: 12 },
    { deviceId: "dev-1828", riskScore: 0.73, category: "high", downtimeHours: 8 },
    { deviceId: "dev-9910", riskScore: 0.44, category: "medium", downtimeHours: 4 }
  ];
}
