import json

import httpx

from schemas.user_schemas import UserCreateSchema
from settings import settings
from fastapi import APIRouter

router = APIRouter(
    tags=["fixtures"],
    prefix="/fixtures"
)


@router.post("/add_users")
async def add_user_fixtures():
    new_user = UserCreateSchema(username="test_user", password="123", last_name="test_last_name",
                                name="test_first_name")

    async with httpx.AsyncClient() as client:
        await client.post(f"{settings.USER_SERVICE_URL}/auth/register",
                          content=json.dumps(new_user.model_dump(by_alias=True)))

    new_user2 = UserCreateSchema(username="test_user2", password="123", last_name="test_last_name2",
                                 name="test_first_name2")

    async with httpx.AsyncClient() as client:
        await client.post(f"{settings.USER_SERVICE_URL}/auth/register",
                          content=json.dumps(new_user2.model_dump(by_alias=True)))
