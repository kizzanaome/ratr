FROM python:3.7.4-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

CMD python users/manage.py run -h 0.0.0.0

