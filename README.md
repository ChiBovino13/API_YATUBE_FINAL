# Проект «API для Yatube»
**Описание**
API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

### Как запустить проект:

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
