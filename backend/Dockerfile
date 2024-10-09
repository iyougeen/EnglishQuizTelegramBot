FROM python:3.11-alpine

EXPOSE 8000

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

RUN chmod a+x docker-entrypoint.sh

ENTRYPOINT ["sh", "docker-entrypoint.sh"]