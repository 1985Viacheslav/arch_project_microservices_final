import httpx
from aiocircuitbreaker import circuit
from fastapi import APIRouter, Depends

from routers.user_router import oauth2_scheme
from response_validator import handle_response
from schemas.message_schemas import MessageSchema
from schemas.ptp_chat_schemas import PtpChatSchema
from settings import settings

router = APIRouter(
    tags=["ptp_chat"],
    prefix="/ptp_chat",
)


@router.post('/send_message/{user_getter_id}')
@circuit(failure_threshold=5, recovery_timeout=30)
async def send_message(message_text: str, user_getter_id: int,
                       token: str = Depends(oauth2_scheme)):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {token}"}
        response = await client.post(
            f"{settings.PTP_CHAT_SERVICE_URL}/ptp_chat/send_message/{user_getter_id}?message_text={message_text}",
            headers=headers)
        return handle_response(response)


@router.get('/get_messages')
@circuit(failure_threshold=5, recovery_timeout=30)
async def get_messages(token: str = Depends(oauth2_scheme)):

    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {token}"}
        response = await client.get(
            f"{settings.PTP_CHAT_SERVICE_URL}/ptp_chat/get_messages",
            headers=headers)
        return handle_response(response)
