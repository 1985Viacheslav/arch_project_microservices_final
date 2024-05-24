import httpx
from fastapi import APIRouter, Depends

from response_validator import handle_response
from routers.user_router import oauth2_scheme
from schemas.group_chat_schemas import GroupChatSchema
from schemas.message_schemas import MessageSchema
from settings import settings

router = APIRouter(
    prefix="/group_chat",
    tags=["group_chat"],
)


# Далее идет реализация эндпоинтов
@router.post("/create")
async def create_group(group_name: str, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.GROUP_CHAT_SERVICE_URL}/group_chat/create?group_name={group_name}",
                                     headers=headers)
        return handle_response(response)


@router.post("/add_member/{group_id}/{user_id}")
async def add_member_to_group(group_id: str, user_id: int, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.GROUP_CHAT_SERVICE_URL}/group_chat/add_member/{group_id}/{user_id}",
                                     headers=headers)
        return handle_response(response)


@router.post("/remove_member/{group_id}/{user_id}")
async def remove_member_from_group(group_id: str, user_id: int, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.GROUP_CHAT_SERVICE_URL}/group_chat/remove_member/{group_id}/{user_id}",
                                     headers=headers)
        return handle_response(response)


@router.post('/send_message/{group_id}')
async def send_message(message_text: str, group_id: str, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.GROUP_CHAT_SERVICE_URL}/group_chat/send_message/{group_id}?message_text={message_text}",
            headers=headers)
        return handle_response(response)


@router.get('/{group_id}')
async def get_group(group_id: str, token: str = Depends(oauth2_scheme)):

    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.GROUP_CHAT_SERVICE_URL}/group_chat/{group_id}",
            headers=headers)

        return handle_response(response)


@router.delete('/{group_id}')
async def delete_group(group_id: str, token: str = Depends(oauth2_scheme)):

    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{settings.GROUP_CHAT_SERVICE_URL}/group_chat/{group_id}",
            headers=headers)
        return handle_response(response)
