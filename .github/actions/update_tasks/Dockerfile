FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.9-slim

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends git pandoc

ENV PATH="/opt/venv/bin:$PATH"

COPY . .
ENTRYPOINT [ "python", "./tasks.py" ]