FROM python:3.8.13-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV OAUTHLIB_INSECURE_TRANSPORT=1

ARG requirements=requirements.txt
ENV DJANGO_SETTINGS_MODULE=codemonk.settings

WORKDIR /app

RUN apt-get update -y

RUN pip install --upgrade pip

COPY requirements.txt/ /app/
RUN pip install -r ${requirements}

COPY runserver.sh/ /app/



COPY . /app/
RUN chmod +x runserver.sh
ENTRYPOINT ["/bin/sh","runserver.sh"]
EXPOSE 8000
