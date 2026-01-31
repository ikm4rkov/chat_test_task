# Пример back-end сервиса для API чатов и приложений

## Описание

Данное приложение — это простой REST API для управления чатами и сообщениями, реализованный с использованием **FastAPI**, **SQLAlchemy**, **PostgreSQL** и **Alembic**.

Функциональность:
- создание чатов
- добавление сообщений в чат
- получение чата с последними сообщениями
- удаление чата (каскадно удаляются сообщения)

Приложение предназначено как тестовое задание и демонстрирует базовую backend‑архитектуру: ORM, миграции, Docker, тестирование.

---

## Стэк программ

- Python 3.10
- FastAPI
- SQLAlchemy 2.x
- PostgreSQL
- Alembic (миграции)
- Pytest (тестирование)
- Docker / Docker Compose

---

## Установка и запуск (Docker)

### Требования (тестировалось на)

- Docker Desktop
- Docker Compose
- PostgreSQL 18.1

Также может быть запущено с помощью устанавливаемый под Linux утилиты Docker

### Сборка и запуск

Из корня проекта выполните:

```bash
cd chat_test_task
docker compose up --build
```

После создания контейнера можно запускать без ключа --build

После успешного запуска:

- API будет доступно по адресу: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

Миграции Alembic применяются автоматически при старте контейнера.

---

## Использование API

### Swagger UI

Откройте в браузере:

```
http://localhost:8000/docs
```

Через интерфейс Swagger можно:
- создать чат
- добавить сообщение
- получить чат с сообщениями
- удалить чат

---

### Примеры запросов через curl

#### Создать чат

```bash
curl -X POST "http://localhost:8000/chats/" \
     -H "Content-Type: application/json" \
     -d '{"title": "Мой первый чат"}'
```

---

#### Добавить сообщение в чат

```bash
curl -X POST "http://localhost:8000/chats/1/messages/" \
     -H "Content-Type: application/json" \
     -d '{"text": "Привет, мир!"}'
```

---

#### Получить чат с сообщениями

```bash
curl "http://localhost:8000/chats/1?limit=20"
```

---

#### Удалить чат

```bash
curl -X DELETE "http://localhost:8000/chats/1"
```

---

## Тестирование

В проекте используется **pytest**.

### Запуск тестов локально

```bash
cd chat_test_task
pip install --no-cache-dir -r requirements.txt
pytest -v
```
**Для запуска локально требуется создать базу данных chat_db с помощью PostgreSQL**

---

### Запуск тестов внутри Docker

Выполните команду:

```bash
docker compose run --rm api pytest -v
```

Контейнер будет запущен временно, выполнит тесты и завершится.

---

## Автор

Выполнил Марков Иван, январь 2026

