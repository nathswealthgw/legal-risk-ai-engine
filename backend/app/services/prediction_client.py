import httpx


class TensorFlowServingClient:
    def __init__(self, url: str) -> None:
        self.url = url

    async def predict(self, features: list[float]) -> float:
        payload = {"instances": [features]}
        async with httpx.AsyncClient(timeout=2.5) as client:
            response = await client.post(self.url, json=payload)
            response.raise_for_status()
        predictions = response.json().get("predictions", [[0.0]])
        return float(predictions[0][0])
