FROM node:6

RUN sed -i 's#deb.debian.org#ba.mirror.garr.it/mirrors#g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y librsvg2-dev
RUN npm install -g mathoid@0.7.1

WORKDIR /usr/local/lib/node_modules/mathoid/

RUN cp config.dev.yaml config.yaml
RUN sed -i 's/speechOn: true/speechOn: false/g' config.yaml
RUN sed -i 's/speakText: true/speakText: false/g' config.yaml
RUN sed -i 's/num_workers: 0/num_workers: ncpu/g' config.yaml

EXPOSE 10044

CMD npm start
