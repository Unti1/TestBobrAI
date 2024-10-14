FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости с помощью Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

# Команда для запуска бота
CMD ["poetry", "run", "python", "main.py"]
