FROM python:3.4
MAINTAINER ContextInformatic <contextinformatic@gmail.com>
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install libpq-dev python3-dev python3-pip git libpng12-dev zlib1g-dev libfreetype6-dev libjpeg-dev libpq-dev mercurial libgeos-dev

RUN mkdir -p /usr/src/app


WORKDIR /usr/src/app

COPY . /usr/src/app


RUN pip3 install -r /usr/src/app/requirements.txt --no-cache-dir
#RUN pip3 install -e git+https://github.com/celery/billiard.git#egg=billiard
#RUN pip3 install -e git+https://github.com/celery/kombu.git#egg=kombu

RUN chmod 777 /usr/src/app/init.sh
RUN chmod +x /usr/src/app/init.sh
#RUN sh /usr/src/app/init.sh


RUN chmod 777 /usr/src/app/celery_start.sh
RUN chmod +x /usr/src/app/celery_start.sh