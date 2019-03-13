# Word Count API
A flask based API that can count the numbers of given keywords. 

## Principle of the API
Use regular expression to get the text without html tag, and also use regular expression to find the keyword. For example, there are several situations that would be accepted ...
- .keyword/
- keyword
- keyword,
- \<b>keyword\</b>

## Prerequisite and Environment 
- Operating system that had been tested: MacOS 10.14, Ubuntu 16.04
- Python == 3.6.*
- Flask == 1.02
- requests == 2.18.4
- SQLAlchemy == 1.2.7

## Getting Started
1. `$ git clone https://github.com/cftang0827/word_count_api.git`
2. `$ cd word_count`
3. install all package you need `$ pip3 install -r requirements.txt`
4. run the app by using localhost and 8000 port`$ python3 app.py localhost`

## Use Docker 
The Dockerfile is provided, you may simply use docker to run the app.

1. `$ cd word_count`
2. Build the docker image  `$ docker build -t flask_word_count .`
3. Build the docker container   `$ docker run -d -p 8000:8000 flask_word_count`

## Documents
There is a complete auto-generated document in `doc/index.html`, and belowed is the simple version of document.
#### Request
- format: JSON (application / json)
- method: POST
```
{
  "word": "fit",
  "url": "http://www.test123.com"
}
```
#### Response
- format: JSON
- status code: 200
```
{
  "count": 6,
  "status": "ok"
}
```
