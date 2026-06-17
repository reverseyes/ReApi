from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    name: str

@app.get("/")
def home():
    return {"message": "what are you doing here? leave. go to /docs"}

@app.post("/api/greet")
def greet_user(data: UserInput):
    return {"message": f"Hello, {data.name}! API is up."}
