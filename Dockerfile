FROM python:3.7-slim-buster
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -yq install dialog apt-utils

RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install build-essential curl python3-dev python3-pip supervisor libpcre3 libpcre3-dev python3-openslide

RUN pip install --upgrade pip
COPY web/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY web/ /app
WORKDIR /app

RUN useradd uwsgi

COPY web/services/supervisord.conf /etc/supervisor/conf.d/uwsgi.conf
COPY web/services/uwsgi/slides.ini /etc/uwsgi/slides.ini

CMD ["/usr/bin/supervisord"]
