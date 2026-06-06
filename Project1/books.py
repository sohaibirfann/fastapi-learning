from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def first_api():
    return {"message": "First Endpoint"}