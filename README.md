# How to start (Linux)

1. Clone git repository and go to a repository folder
```shell
git clone https://github.com/iyougeen/EnglishQuizTelegramBot.git && cd EnglishQuizTelegramBot
```
2. Copy .env.example file to .env file
```shell
cp .env.example .env
```
3. In .env file
  - set DJANGO_SECRET_KEY variable with your secret key.
  - set DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL with your values to create Django superuser.
  - if you need you can change other env variables on your own values.

4. Then compose and build docker project
```shell
docker compose -f docker-compose-dev.yml up -d --build
```
