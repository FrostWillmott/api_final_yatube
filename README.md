
# api_final

## Описание
Yatube API — это RESTful API для социальной медиа платформы, где пользователи могут создавать посты, комментировать посты, подписываться на других пользователей и вступать в группы.

## Установка
Чтобы развернуть проект на локальной машине, выполните следующие шаги:

1. **Клонируйте репозиторий:**

    git clone https://github.com/FrostWillmott/yatube_api.git
    cd yatube_api


2. **Создайте и активируйте виртуальное окружение:**

    python3 -m venv venv
    source venv/bin/activate  # В Windows используйте `venv\Scripts\activate`


3. **Установите зависимости:**

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt


4. **Примените миграции:**

    python manage.py migrate


5. **Запустите сервер разработки:**

    python manage.py runserver


## Примеры
Вот несколько примеров запросов к API:

1. **Получить все посты:**

    GET /api/v1/posts/


2. **Создать новый пост:**

    POST /api/v1/posts/
    {
        "text": "Это новый пост",
        "group": 1
    }


3. **Получить комментарии к посту:**

    GET /api/v1/posts/{post_id}/comments/


4. **Подписаться на пользователя:**

    POST /api/v1/follow/
    {
        "following": "username"
    }


5. **Получить все группы:**

    GET /api/v1/groups/
