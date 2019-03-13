FROM ubuntu:16.04
LABEL MAINTAINER cftang <cftang0827@gmail.com>

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]