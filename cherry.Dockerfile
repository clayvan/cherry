FROM python:3.7-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache --virtual build-base gcc python3-dev libffi-dev musl-dev openssl-dev
RUN pip install kubernetes prometheus-client Flask

COPY ./cherry.py /cherry/cherry.py

ENTRYPOINT ["python", "/cherry/cherry.py"]
