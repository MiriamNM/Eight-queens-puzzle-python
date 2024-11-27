FROM python:3.11

WORKDIR /app

COPY . /app

COPY ./src /app/src

COPY requirements.txt .

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --upgrade pip

EXPOSE 8080

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

ENV PYTHONPATH=/app/src

ENV TZ=America/Mexico_City