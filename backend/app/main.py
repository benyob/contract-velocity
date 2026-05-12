from fastapi import FastAPI
from app.routes.contracts import router as contract_router

app = FastAPI(title="Contract Review Accelerator")

app.include_router(contract_router)

@app.get("/")
def root():
    return {"status": "running"}