from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    MONGO_HOST: str
    API_GATEWAY_URL: str
    USER_SERVICE_URL: str
    PTP_CHAT_SERVICE_URL: str
    GROUP_CHAT_SERVICE_URL: str
    SECRET_KEY_AUTH: str
    SECRET_KEY_JWT: str
    REDIS_HOST: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    class Config:
        env_file = ".env"


settings = Settings()
