FROM python:3.12.4-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/backend

RUN gcc -shared -o libfactorial.so -fPIC factorial.c

WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]
