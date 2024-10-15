# Используйте официальный образ Python в качестве базового
FROM python:3.11

# Установите переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файл требований
COPY requirements.txt /app/

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте все файлы проекта в контейнер
COPY . /app/

CMD ["python", "orders_project/manage.py", "fill_db"]

# Запустите команду для создания базы данных при старте контейнера
CMD ["python", "orders_project/manage.py", "runserver", "0.0.0.0:8000"]
