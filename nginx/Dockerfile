FROM nginx:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -yq install curl supervisor

RUN rm /etc/nginx/conf.d/default.conf

COPY slides.conf /etc/nginx/conf.d/default.conf
