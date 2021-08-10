# Для запуска приложения наберите в коммандной строке:
# docker build . -t homework_03
# docker run -d -p 8000:8000 homework_03

FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY . ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]