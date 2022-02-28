FROM python:3.9-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.9-slim

COPY --from=builder /opt/venv /opt/venv

WORKDIR /github/workspace/

RUN apt-get update && \
    apt-get install -y --no-install-recommends git pandoc tree

ENV PATH="/opt/venv/bin:$PATH"

COPY . .
RUN pwd && ls -lA && tree ..
ENTRYPOINT [ "python", "tasks.py" ]
RUN pwd && ls -lA && tree ..
