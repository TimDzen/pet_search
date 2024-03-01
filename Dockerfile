FROM python:3-alpine

WORKDIR /app/django

COPY /pet_search .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1


RUN python ./pet_search/manage.py migrate

CMD ["python", "./pet_search/manage.py", "runserver", "0.0.0.0:8080"]