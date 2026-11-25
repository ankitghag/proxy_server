from fastapi import APIRouter, Request
import os

# from app.modules.users.schemas import UserResponse
# from app.modules.users.service import UserService


user_router = APIRouter(prefix="/user")
import asyncio

# service = UserService()
APP_PORT = int(os.getenv("APP_PORT", "8000"))


@user_router.get("/demo")
async def get_demo(request: Request):
    print(APP_PORT)
    # if APP_PORT == 8001:
    #     await asyncio.sleep(30)
    return "HELLO WORLD"

# @router.get("/{user_id}", response_model=UserResponse)
# def get_user(user_id: int):
#     return service.get_user(user_id)
