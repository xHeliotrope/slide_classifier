FROM python:3.7-slim-buster
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -yq install dialog apt-utils 

RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install build-essential curl python-dev python3-dev python3-pip supervisor libpcre3 libpcre3-dev

COPY web/ /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY web/config/supervisord.conf /etc/supervisord.conf
COPY web/config/uwsgi/slides.ini /etc/uwsgi/slides.ini

CMD ["/usr/bin/supervisord"]
