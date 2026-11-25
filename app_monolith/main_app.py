from fastapi import FastAPI, Request

from modules.users.router import user_router
import asyncio

app = FastAPI(title="My FastAPI Application")

app.include_router(
    user_router,
    # prefix="/user",
    tags=["Users"],
)

@app.get("/health")
async def get_health(request: Request):
    return {"status_code": 200}

