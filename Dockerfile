FROM python:3.11

WORKDIR /app

COPY ./src /app/src

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade pip

EXPOSE 5000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]

