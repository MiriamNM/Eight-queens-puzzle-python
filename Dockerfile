FROM python:3-11-slim

WORKDIR /app

COPY requirements.txt :/

COPY ./src /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]
