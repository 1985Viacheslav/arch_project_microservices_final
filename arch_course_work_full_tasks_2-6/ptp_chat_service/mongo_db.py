import motor.motor_asyncio
from settings import settings

url = f'mongodb://{settings.MONGO_INITDB_ROOT_USERNAME}:{settings.MONGO_INITDB_ROOT_PASSWORD}@{settings.MONGO_HOST}:27017'

# Подключение к MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(
    url,
    uuidRepresentation="standard"
)

db = client['chats']

# Получение коллекций наших моделей

PtpChat = db['ptp_chat']
