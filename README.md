ЯП - Спринт 9 - Проект «API для Yatube». Python-разработчик (бекенд) (Яндекс.Практикум)
Описание
API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Стек технологий
Python 3.11,
Django 4.2,
DRF,
JWT + Djoser
Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке.
Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
Затем нужно установить все зависимости из файла requirements.txt
cd yatube_api
pip install -r requirements.txt
Выполняем миграции:
python manage.py migrate
Создаем суперпользователя:
python manage.py createsuperuser
Запускаем проект:
python manage.py runserver
Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
Примеры работы с API для авторизованных пользователей
Для создания публикации используем:
POST /api/v1/posts/
в body

{
"text": "string",
"image": "string",
"group": 0
}
Обновление публикации:
PUT /api/v1/posts/{id}/
в body

{
"text": "string",
"image": "string",
"group": 0
}
Частичное обновление публикации:
PATCH /api/v1/posts/{id}/
в body

{
"text": "string",
"image": "string",
"group": 0
}
Частичное обновление публикации:
DEL /api/v1/posts/{id}/
Получение доступа к эндпоинту /api/v1/follow/ (подписки) доступен только для авторизованных пользователей.

подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.

GET /api/v1/follow/
Авторизованные пользователи могут создавать посты, комментировать их и подписываться на других пользователей.
Пользователи могут изменять(удалять) контент, автором которого они являются.
Добавить группу в проект нужно через админ панель Django:
после авторизации, переходим в раздел Groups и создаем группы.

admin/
Доступ авторизованным пользователем доступен по JWT-токену (Joser), который можно получить выполнив POST запрос по адресу:
POST /api/v1/jwt/create/
Передав в body данные пользователя (например в postman):
{
"username": "string",
"password": "string"
}
Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:
Authorization: Bearer {your_token}
Обновить JWT-токен:
POST /api/v1/jwt/refresh/
Проверить JWT-токен:
POST /api/v1/jwt/verify/
Так же в проекте API реализована пагинация (LimitOffsetPagination):
GET /api/v1/posts/?limit=5&offset=0
Автор:
