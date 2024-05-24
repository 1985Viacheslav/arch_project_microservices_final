import httpx
from fastapi import APIRouter, HTTPException

from settings import settings

router = APIRouter(
    tags=['fixtures'],
    prefix='/fixtures'
)


@router.post('/')
async def add_fixtures():
    """
    Создание тестовых данных
    """

    try:
        await add_user_fixtures()
        await add_group_ptp_fixtures()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def add_user_fixtures():
    async with httpx.AsyncClient() as client:
        await client.post(f"{settings.USER_SERVICE_URL}/fixtures/add_users")


async def add_group_ptp_fixtures():
    async with httpx.AsyncClient() as client:
        await client.post(f"{settings.PTP_CHAT_SERVICE_URL}/fixtures/add_ptp_chat")

    async with httpx.AsyncClient() as client:
        await client.post(f"{settings.GROUP_CHAT_SERVICE_URL}/fixtures/add_group_chat")
