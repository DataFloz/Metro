FROM python:3.9-slim

WORKDIR /app

COPY ./runner /app/runner
COPY ./pipeline /app/pipeline

RUN pip install -r ./runner/requirements.txt

ENTRYPOINT ["python", "./runner/main.py"]