FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

EXPOSE 8000

CMD python manage.py runserver