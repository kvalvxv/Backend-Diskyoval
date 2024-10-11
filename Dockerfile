# Dockerfile Alternativo con libmariadb-dev-compat
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev-compat \
    libpq-dev \
    gcc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
