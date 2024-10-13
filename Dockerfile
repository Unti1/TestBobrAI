# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости для работы с Poetry
RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем путь Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости с помощью Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

# Команда для запуска бота
CMD ["poetry", "run", "python", "main.py"]
