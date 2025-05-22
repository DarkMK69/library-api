Библиотечный API (FastAPI + PostgreSQL)

Описание проекта

RESTful API для управления библиотечным каталогом с возможностями:

📚 Управление книгами (CRUD)

👥 Управление читателями

🔐 JWT-аутентификация библиотекарей

📖 Логика выдачи/возврата книг с проверкой бизнес-правил

Технологии

Python 3.10+

FastAPI (веб-фреймворк)

PostgreSQL (база данных)

SQLAlchemy (ORM)

Alembic (миграции)

JWT (аутентификация)

Установка и запуск

1. Требования

Установленный Python 3.10+

PostgreSQL 13+

Git (опционально)

2. Клонирование репозитория

bash

git clone https://github.com/ваш-репозиторий/library_api.git

cd library_api

3. Настройка окружения

Создайте файл .env в корне проекта:

ini

DATABASE_URL=postgresql+asyncpg://user:password@localhost/library_db

SECRET_KEY=ваш-секретный-ключ

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

4. Установка зависимостей

bash

pip install -r requirements.txt

5. Настройка базы данных

Создайте БД в PostgreSQL:

sql

CREATE DATABASE library_db;

Примените миграции:

bash

alembic upgrade head

6. Запуск сервера

bash

uvicorn app.main:app --reload

API будет доступно по адресу: http://127.0.0.1:8000

Документация API

После запуска доступны:

📄 Swagger UI: http://127.0.0.1:8000/docs

📄 ReDoc: http://127.0.0.1:8000/redoc

Основные эндпоинты

Аутентификация

POST /api/v1/auth/register - Регистрация библиотекаря

POST /api/v1/auth/login - Получение JWT-токена

Книги (требуют аутентификации)


POST /api/v1/books - Добавить книгу

GET /api/v1/books - Список всех книг

GET /api/v1/books/{id} - Получить книгу по ID

PUT /api/v1/books/{id} - Обновить книгу

DELETE /api/v1/books/{id} - Удалить книгу

Читатели

POST /api/v1/readers - Добавить читателя

GET /api/v1/readers/{id} - Получить читателя

Выдача книг
POST /api/v1/borrows - Выдать книгу читателю

PUT /api/v1/borrows/{id}/return - Вернуть книгу

Бизнес-правила

❗ Книгу можно выдать только если есть доступные экземпляры

❗ Читатель не может иметь более 3 книг одновременно

❗ Нельзя вернуть уже возвращенную книгу

Тестирование

Запуск тестов:

bash

pytest

Разработчику

Создание новой миграции

bash

alembic revision --autogenerate -m "Описание изменений"

alembic upgrade head

Структура проекта

library_api/

├── app/               # Основной код

│   ├── api/           # Эндпоинты

│   ├── core/          # Настройки

│   ├── db/            # Модели БД

│   ├── schemas/       # Pydantic схемы

│   └── services/      # Бизнес-логика

├── tests/             # Тесты

└── migrations/        # Миграции Alembic
