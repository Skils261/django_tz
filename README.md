# Orders Project

Это Django проект для управления продуктами и заказами. Проект выводит таблицу с продуктами, которая содержит следующую информацию:
- ID
- Название товара
- Категория
- Статус активности (Active/Inactive)
- Цена
- Количество заказов за предыдущий месяц
- Количество заказов за текущий месяц

## Основные функции
- Подсчет количества заказов за прошлый и текущий месяцы через специальные методы в модели.
- Вывод таблицы с продуктами и их характеристиками на веб-странице.
- Админка для управления продуктами и заказами.

## Установка и настройка

### 1. Клонирование репозитория

Клонируйте проект на локальный компьютер:

```bash
git clone https://github.com/Skils261/django_tz.git
cd orders_project
```

### 2. Создание виртуального окружения

Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate  # Для Windows
```

### 3. Установка зависимостей

Установите все необходимые зависимости:

```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных
По умолчанию используется база данных SQLite. Вы можете настроить другую СУБД, отредактировав файл settings.py в разделе DATABASES.

Примените миграции, чтобы создать таблицы в базе данных:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Заполнение начальными данными
Вы можете заполнить базу данных начальными данными двумя способами:

a. Загрузка данных через фикстуры:
bash
Копировать код
python manage.py loaddata initial_data.json
b. Запуск скрипта для генерации данных:
Используйте команду для автоматического создания данных продуктов и заказов:


```bash
python manage.py fill_db
```

### 6. Запуск проекта
После того, как база данных настроена, можно запустить сервер:

```bash
python manage.py runserver
```

Проект будет доступен по адресу: http://127.0.0.1:8000.

## Админка

Для доступа к админке создайте суперпользователя:

```bash
python manage.py createsuperuser
```

Перейдите на http://127.0.0.1:8000/admin и войдите под учетной записью суперпользователя.
