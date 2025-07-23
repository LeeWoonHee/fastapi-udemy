from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

# ep11 udemy
@app.get("/shipment/{id}")
async def get_shipment(id : int) -> dict[str, str | int]:
    return {"content": "wooden table", "status": "in transit", "id": id}


@app.get("/scalar", include_in_schema=False) 
async def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="scalar api")
