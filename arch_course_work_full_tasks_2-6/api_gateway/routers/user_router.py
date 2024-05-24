import json

import httpx
from fastapi import APIRouter, Depends, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from response_validator import handle_response
from schemas.user_schemas import Token, UserReadSchema, UserCreateSchema, UserUpdateSchema
from settings import settings

router = APIRouter(

)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.post("/auth/token", tags=['auth'])
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    form_data_dict = form_data.__dict__

    data = {
        "grant_type": form_data_dict.get("grant_type"),
        "username": form_data_dict.get("username"),
        "password": form_data_dict.get("password"),
        "scope": form_data_dict.get("scope"),
        "client_id": form_data_dict.get("client_id"),
        "client_secret": form_data_dict.get("client_secret"),
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.USER_SERVICE_URL}/auth/token", data=data)
        return handle_response(response)


@router.post('/auth/refresh', tags=['auth'])
async def refresh_token(token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.USER_SERVICE_URL}/auth/refresh", headers=headers)
        return handle_response(response)


@router.post('/auth/logout', tags=['auth'])
async def logout(token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.USER_SERVICE_URL}/auth/refresh", headers=headers)
        return handle_response(response)


@router.post('/auth/register', tags=['auth'])
async def create_new_user(new_user: UserCreateSchema):
    data = new_user.model_dump(by_alias=True)


    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.USER_SERVICE_URL}/auth/register", content=json.dumps(data))
        return handle_response(response)


@router.get('/user/me', status_code=status.HTTP_200_OK, tags=['user'])
async def get_me(token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}


    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.USER_SERVICE_URL}/user/me", headers=headers)
        return handle_response(response)


@router.patch('/user/me', status_code=status.HTTP_202_ACCEPTED, tags=['user'])
async def update_me(new_data: UserUpdateSchema, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    data = new_data.model_dump(by_alias=True)

    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{settings.USER_SERVICE_URL}/user/me", headers=headers,
                                      content=json.dumps(data))
        return handle_response(response)


@router.delete('/user/me', status_code=status.HTTP_204_NO_CONTENT, tags=['user'])
async def delete_me(token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{settings.USER_SERVICE_URL}/user/me", headers=headers)
        return handle_response(response)


@router.get('/user/search/{mask}', tags=['user'])
async def get_user_by_mask(mask: str, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.USER_SERVICE_URL}/user/search/{mask}", headers=headers)
        return handle_response(response)


@router.get('/user/', tags=['user'])
async def get_user_by_username(username: str, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.USER_SERVICE_URL}/user/?username={username}", headers=headers)
        return handle_response(response)


@router.get('/user/get/{user_id}', tags=['user'])
async def search_user(user_id: int, token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.USER_SERVICE_URL}/user/get/{user_id}", headers=headers)
        return handle_response(response)
