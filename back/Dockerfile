FROM python:3.10

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY ./app /usr/src/app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5174"]