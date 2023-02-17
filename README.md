# Проект «𝔸ℙ𝕀 для 𝕐𝕒𝕥𝕦𝕓𝕖»
____
**Описание:**
API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.
____
**Технологии:**
[image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
[image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
[image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
[image](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
### 🎉🐚  Как запустить проект  ⛵♣

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ChiBovino13/api_final_yatube.git
```

```
cd API_FINAL_YATUBE
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
. venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
python3 manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```


# Примеры работы с 𝔸ℙ𝕀 для всех пользователей:
Публикция, редактирование и удаление контента доступно только авторизированным пользователям.
Неавторизированные пользователи могут работать с API только в режиме чтения.

```
GET api/v1/posts/ - список постов;
GET api/v1/posts/{id}/ - страница конкретного поста по его id;
GET api/v1/groups/ - список групп;
GET api/v1/groups/{id}/ - страница конкретной группы по ее id;
GET api/v1/{post_id}/comments/ - список комментариев в конкретному посту;
GET api/v1/{post_id}/comments/{id}/ - конкретный комментарий по его id.
```
## Примеры запросов и ответов

### Создание поста:
```
POST /api/v1/posts/
в body

{
"text": "string"
}
```
### Обновление поста:
```
PUT /api/v1/posts/{id}/
в body

{
"text": "string1"
}
```
### Удаление поста:
```
DEL /api/v1/posts/{id}/
```

### Создание суперпользователя и получение токена:

В терминале:
```
python manage.py createsuperuser

username: admin
password: admin
```
Получить токен через postman:
```
POST /api/v1/jwt/create/
В body:
{
"username": "admin",
"password": "admin"
}
Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:
Authorization: Bearer {your_token}
```

**А̳в̳т̳о̳р̳:̳** [Дарья Горячева](https://github.com/ChiBovino13)
