FROM python:3.4
MAINTAINER ContextInformatic <contextinformatic@gmail.com>
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
# RUN apt-get install gettext
# RUN apt-get install nodejs npm
# RUN npm install -g less
RUN apt-get -y install libpq-dev python3-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY server/ /usr/src/app
COPY theme_configs.py /usr/src/app/erp_cms/theme_configs.py
COPY templates/ /usr/src/templates
COPY static/ /usr/src/static

RUN pip3 install -r /usr/src/app/requirements.txt --no-cache-dir

RUN chmod 777 /usr/src/app/init.sh
RUN chmod +x /usr/src/app/init.sh
#RUN sh /usr/src/app/init.sh

#EXPOSE 8000
#ENV PORT 8000