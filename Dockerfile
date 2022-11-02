FROM python:3.8

WORKDIR /api

ADD . /api

RUN apt update -y  &&  apt upgrade -y && apt-get update

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME NativeHelperApi

CMD ["python", "-u", "api.py"]
