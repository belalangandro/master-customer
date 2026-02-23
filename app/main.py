from fastapi import FastAPI

app = FastAPI(title="Master Customer Service")

@app.get("/")
async def read_root():
    return {"Hello": "Master Customer"}

@app.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    # Ini sengaja dibuat agak sederhana untuk nanti di-review oleh Qwen
    return {"customer_id": customer_id, "name": "John Doe"}