FROM blang/latex:ubuntu

ENV PYTHONUNBUFFERED=True
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-setuptools
RUN apt-get install -y ca-certificates
RUN easy_install3 pip

ADD requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

ENTRYPOINT flask run --host=0.0.0.0 --port=8089
ADD app.py /opt/
