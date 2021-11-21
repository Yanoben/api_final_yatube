# API for social media 'Yatube'

### Технологии в проекте
- Python 3.7
- Django 2.2.19

### Запуск проекта в dev-режиме
- Сначала клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yanoben/yatube_project.git
```

- Установите и активируйте виртуальное окружение
```
python -m venv venv

. venv/bin/activate
```

- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 

- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
### Авторы
Me))



## Installing

    git clone https://github.com/Yanoben/api_final_yatube


## Install reuqirements.txt

    pip3 install -r requirements.txt

## And Run
    python manage.py runserver



### Request

`GET /posts/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/posts/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [

    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    },
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    },
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    }

    ]

### Request

`GET /posts/<int:post_id>/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/posts/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [
        {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
        }
    ]
