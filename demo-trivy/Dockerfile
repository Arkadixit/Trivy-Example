FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY app.py ./app.py

# Fichier contenant un secret fictif
COPY demo-secret.txt ./demo-secret.txt

# Mauvaise configuration volontaire
USER root

EXPOSE 5000

CMD ["python", "app.py"]