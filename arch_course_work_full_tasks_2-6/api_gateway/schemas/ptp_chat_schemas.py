from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from schemas.message_schemas import MessageSchema
from schemas.user_schemas import UserReadSchema


class PtpChatSchema(BaseModel):
    """
    Создаем схему для хранения PTP-чата
    """
    id: PydanticObjectId | None = Field(validation_alias='_id', default=None)
    user_sender: UserReadSchema
    user_getter: UserReadSchema
    messages: list[MessageSchema] | None = []
