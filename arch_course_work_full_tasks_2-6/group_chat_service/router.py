import httpx
from aiocircuitbreaker import circuit
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException

from helpers import get_current_auth_user, oauth2_scheme
from mongo_db import GroupChat
from schemas import GroupChatSchema, MessageSchema, UserReadSchema
from settings import settings
from utils import convert_group_model_to_dict

# Создание маршрутов

router = APIRouter(
    tags=["group_chat"],
    prefix="/group_chat",
)


# Далее идет реализация эндпоинтов
@router.post("/create", response_model=GroupChatSchema)
@circuit(failure_threshold=5, recovery_timeout=30)
async def create_group(group_name: str, username: str = Depends(get_current_auth_user),
                       token: str = Depends(oauth2_scheme)):
    """
    Получаем имя группы и пользователя,
    затем создаем новый объект(групповой чат) в базе данных и возвращаем его

    """

    try:

        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            response = await client.get(f"{settings.USER_SERVICE_URL}/user/?username={username}", headers=headers)
            user = response.json()

        group_chat = GroupChatSchema(group_name=group_name, members=[user])
        new_group = await GroupChat.insert_one(group_chat.model_dump(by_alias=False, exclude={'id'}))

        group = await GroupChat.find_one({"_id": new_group.inserted_id})

        return group

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_member/{group_id}/{user_id}", response_model=GroupChatSchema)
@circuit(failure_threshold=5, recovery_timeout=30)
async def add_member_to_group(group_id: str, user_id: int, token: str = Depends(oauth2_scheme)):
    """
    Получаем id группы и id пользователя,
    затем добавляем пользователя в группу и возвращаем измененный объект(групповой чат)

    """
    try:

        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            response = await client.get(f"{settings.USER_SERVICE_URL}/user/get/{user_id}", headers=headers)
            user = UserReadSchema.model_validate(response.json())

        group = GroupChatSchema.model_validate(await GroupChat.find_one({"_id": ObjectId(group_id)}),
                                               from_attributes=True)

        if user not in group.members:
            group.members.append(user)

        group = await convert_group_model_to_dict(group)

        await GroupChat.update_one({'_id': ObjectId(group.id)},
                                   {'$set': {'members': group.members}})

        upd_group = await GroupChat.find_one({"_id": ObjectId(group_id)})

        return upd_group

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/remove_member/{group_id}/{user_id}", response_model=GroupChatSchema)
@circuit(failure_threshold=5, recovery_timeout=30)
async def remove_member_from_group(group_id: str, user_id: int, token: str = Depends(oauth2_scheme)):
    try:
        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            response = await client.get(f"{settings.USER_SERVICE_URL}/user/get/{user_id}", headers=headers)
            user = UserReadSchema.model_validate(response.json())

        group = GroupChatSchema.model_validate(await GroupChat.find_one({"_id": ObjectId(group_id)}),
                                               from_attributes=True)
        if user in group.members:
            group.members.remove(user)

        group = await convert_group_model_to_dict(group)

        await GroupChat.update_one({'_id': ObjectId(group.id)}, {'$set': {'members': group.members}})
        upd_group = await GroupChat.find_one({"_id": ObjectId(group_id)})

        return upd_group

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/send_message/{group_id}', response_model=MessageSchema)
@circuit(failure_threshold=5, recovery_timeout=30)
async def send_message(message_text: str, group_id: str, username: str = Depends(get_current_auth_user),
                       token: str = Depends(oauth2_scheme)):
    """
    Получаем id группы и сообщение, сообщение добавляется в группу и возвращаем измененный объект(групповой чат)

    """
    try:

        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            response = await client.get(f"{settings.USER_SERVICE_URL}/user/?username={username}", headers=headers)
            user = response.json()

        message = MessageSchema(text=message_text, user=user)
        group = GroupChatSchema.model_validate(await GroupChat.find_one({"_id": ObjectId(group_id)}),
                                               from_attributes=True)
        group.messages.append(message)
        group = await convert_group_model_to_dict(group)

        await GroupChat.update_one({'_id': ObjectId(group.id)},
                                   {'$set': {'messages': group.messages}})

        return message

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/{group_id}', dependencies=[Depends(get_current_auth_user)], response_model=GroupChatSchema)
@circuit(failure_threshold=5, recovery_timeout=30)
async def get_group(group_id: str):
    """
    Получаем id группы, возвращаем объект(групповой чат)

    """

    try:
        group = await GroupChat.find_one({'_id': ObjectId(group_id)})

        if group is None:
            raise HTTPException(status_code=404, detail="Group not found")

        return group

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/{group_id}', dependencies=[Depends(get_current_auth_user)])
@circuit(failure_threshold=5, recovery_timeout=30)
async def delete_group(group_id: str):
    try:
        await GroupChat.delete_one({'_id': ObjectId(group_id)})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
