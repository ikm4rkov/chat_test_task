FROM python:3.10-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN echo "deb http://mirror.yandex.ru/debian trixie main contrib non-free non-free-firmware" > /etc/apt/sources.list && \
    echo "deb http://mirror.yandex.ru/debian trixie-updates main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    echo "deb http://mirror.yandex.ru/debian-security trixie-security main contrib non-free non-free-firmware" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Default command:
# 1) run migrations
# 2) start uvicorn
CMD alembic upgrade head && \
    uvicorn chat_test_task.main:app \
    --host 0.0.0.0 \
    --port 8000