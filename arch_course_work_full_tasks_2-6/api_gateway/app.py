from fastapi import FastAPI

from routers.group_chat_router import router as group_router
from routers.user_router import router as user_router
from routers.ptp_chat_router import router as ptp_router
from fixtures import router as add_fixtures

app = FastAPI(
    title="API Gateway",
)

app.include_router(user_router)
app.include_router(group_router)
app.include_router(ptp_router)
app.include_router(add_fixtures)
