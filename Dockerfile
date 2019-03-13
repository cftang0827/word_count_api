FROM ubuntu:16.04
LABEL MAINTAINER cftang <cftang0827@gmail.com>

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
ADD . /app
WORKDIR /app/app
RUN pip3 install -r ../requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py", "0.0.0.0"]