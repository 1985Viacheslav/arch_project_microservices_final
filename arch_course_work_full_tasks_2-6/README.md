# course_work


### Подготовка

Перед стартом проекта создаём .env файл в корне проекта по примеру ниже.

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=course_work
MONGO_HOST=mongo
MONGO_INITDB_ROOT_USERNAME=mongo
MONGO_INITDB_ROOT_PASSWORD=mongo123
SECRET_KEY_AUTH=efewf3@1fwefw!edwgwerg
SECRET_KEY_JWT=21423rEFEWF2e1vDG21
REDIS_HOST=redis
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=30
API_GATEWAY_URL=http://api_gateway:8000
USER_SERVICE_URL=http://user_service:8080
PTP_CHAT_SERVICE_URL=http://ptp_chat_service:8090
GROUP_CHAT_SERVICE_URL=http://group_chat_service:8070

```

### Запуск

Запуск проекта производится с помощью команды в терминале: docker compose --env-file .env up --build -d

### Открыть
http://localhost:8000/docs#/

### Добавление фикстур

```
Чтобы добавить фикстуры необходимо выполнить запрос методом POST /fixtures при первом запуске проекта, до выполнения остальных
эндпоинтов.
```

