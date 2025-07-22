from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


@app.get("/shipment")
async def get_shipment():
    return {"content": "wooden table", "status": "in transit"}


@app.get("/scalar", include_in_schema=False) 
async def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="scalar api")
