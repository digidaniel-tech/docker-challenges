FROM python:3.12.5-slim-bookworm

RUN pip install flask sqlalchemy pg8000 flask_restful

COPY ./app /app

WORKDIR /app

ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
