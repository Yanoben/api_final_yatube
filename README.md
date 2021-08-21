
## API for social media 'Yatube'


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
