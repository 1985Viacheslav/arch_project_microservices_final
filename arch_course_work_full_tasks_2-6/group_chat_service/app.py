from fastapi import FastAPI
from router import router as chat_router
from fixtures import router as fixtures_router

app = FastAPI(
    title='group_chat_service',
)

app.include_router(chat_router)
app.include_router(fixtures_router)
