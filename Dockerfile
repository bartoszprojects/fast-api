FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./app /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

#RUN python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

#RUN python3 -m alembic upgrade head