FROM python:3.11

WORKDIR /app

COPY . /app

COPY ./src /app/src

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get install -y wget && \
    wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/9.9.0/flyway-commandline-9.9.0-linux-x64.tar.gz | tar xz -C /opt/ && \
    ln -s /opt/flyway-9.9.0/flyway /usr/local/bin/flyway

EXPOSE 5000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080", "python", "app.py", "tail", "-f", "/dev/null"]

ENV PYTHONPATH=/app/src

ENV TZ=America/Mexico_City