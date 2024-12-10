import { useEffect, useState } from "react";
import { fetchRiskData, RiskItem } from "../services/api";

export function useRiskData() {
  const [items, setItems] = useState<RiskItem[]>([]);

  useEffect(() => {
    fetchRiskData().then(setItems);
  }, []);

  return items;
}
