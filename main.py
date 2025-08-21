from typing import Any

from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from starlette.status import HTTP_406_NOT_ACCEPTABLE

app = FastAPI()

# ep14 udemy
shipments = {
    123: {"weight": 95, "content": "book", "status": "in transit"},
    456: {"weight": 2.5, "content": "phone", "status": "delivered"},
    789: {"weight": 15, "content": "laptop", "status": "processing"},
    321: {"weight": 0.8, "content": "headphones", "status": "shipped"},
    654: {"weight": 25, "content": "chair", "status": "pending"},
    987: {"weight": 3.2, "content": "tablet", "status": "in transit"},
    147: {"weight": 45, "content": "monitor", "status": "delivered"},
}


# @app.get("/shipment/latest")
# async def get_latest_shipment() -> dict[str, Any]:
#     id = max(shipments.keys())
#     return shipments[id]


# 쿼리 파라미터로 하고 싶을 떄는 /{id} 제거 하면 자동으로 query 파라미터로 인식함
@app.get("/shipment", status_code=status.HTTP_200_OK)
async def get_shipment(id: int | None = None) -> dict[str, Any]:
    # if not id:
    #     id = max(shipments.keys())
    #     return shipments[id]
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id not found"
        )
    return shipments[id]


# ep16 udemy
@app.post("/shipment")
def submit_shipment(content: str, weight: float) -> dict[str, int]:


    if weight > 25 :
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="용량제한")
    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {"content": content, "weight": weight, "status": "placed"}
    return{ "id" : new_id}

@app.get("/scalar", include_in_schema=False)
async def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="scalar api")
