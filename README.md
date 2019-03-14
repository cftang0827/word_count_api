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

## Discussion
1. About the algorithm to find the keyword in website.
There are two methods that I can use and I use the one of them. First one is using *BeautifulSoup* to parse the HTML content and use regex to find the keyword. And second one is just using regex to filter out the html tag and use another regex to find the keyword. I chose the second method, but if there's more time, I think first method could be implemented and compare the result.

2. About the cache to reduce the computer power of server. 
I use sqlite DB to save the record of analysis, however, I think it may not be a best choice. As a cache-based usage, it would be better to use the faster database, for example NoSQL DB such like *DynamoDB* or even faster *Redis*. But this time I do not have so much time to do so. If Redis is used, the architecture would be a little bi different. I will not only save the record via SQL table but also save a Redis one. And for every request, I will check Redis first to check whether is there any same query before, and it's a efficient way as a cache. 

3. For more stable design
Even the keyword counter is not a really heavy job, the thinking of scalibility would be still helpful. If there are more than 10000 requests in one time, the server will crash. Therefore, a way of load-balancing would be important. For example, we can use nginx to do load balancing, and also we could use ASG on AWS. Also, we can design our app as a worker pattern, use message queue such like SQS on AWS or RabbitMQ, we can easily set up the worker and producer architecture to deal with high demanded moment and sustain high availability.

4. However, my current DB is just a simple sqlite, if we want to make whole system scalable and sustain HA, we need to use a SQL server and use connection pool to prevent from too many db connections in one time. 
