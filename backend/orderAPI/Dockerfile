# Используем официальный образ Python
FROM python:3.9

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Создаем и переходим в рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем сервер Django (можно заменить на gunicorn в production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]