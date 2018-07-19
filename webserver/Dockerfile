FROM python:3.6.6-alpine3.8

ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENV FLASK_RUN_PORT 8888

RUN apk add bash gcc musl-dev mysql mariadb-dev
RUN mkdir /webserver/
ADD requeriments.txt /webserver/requeriments.txt
RUN pip install -r /webserver/requeriments.txt 

EXPOSE 8888

WORKDIR /webserver/
ENTRYPOINT [ "python", "-m", "flask", "run" ]
