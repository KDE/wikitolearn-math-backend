FROM nginx:latest

RUN sed -i 's#deb.debian.org#ba.mirror.garr.it/mirrors#g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y ca-certificates

ARG SERVICE_PORT
ENV SERVICE_PORT=${SERVICE_PORT}
EXPOSE ${SERVICE_PORT}

COPY nginx.conf /etc/nginx/nginx.conf
RUN sed -i "s/SERVICE_PORT/$SERVICE_PORT/g" /etc/nginx/nginx.conf
