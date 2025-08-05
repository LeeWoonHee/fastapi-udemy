from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

# ep13 udemy
shipments = {
    123: {"weight": 95, "content": "book", "status": "in transit"},
    456: {"weight": 2.5, "content": "phone", "status": "delivered"},
    789: {"weight": 15, "content": "laptop", "status": "processing"},
    321: {"weight": 0.8, "content": "headphones", "status": "shipped"},
    654: {"weight": 25, "content": "chair", "status": "pending"},
    987: {"weight": 3.2, "content": "tablet", "status": "in transit"},
    147: {"weight": 45, "content": "monitor", "status": "delivered"},
}


@app.get("/shipment/latest")
async def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]


@app.get("/shipment/{id}")
async def get_shipment(id: int) -> dict[str, Any]:
    if id not in shipments:
        return {"detail": "shipment not found"}
    return shipments[id]


@app.get("/scalar", include_in_schema=False)
async def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="scalar api")
