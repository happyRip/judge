FROM python:3.9-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


FROM python:3.9-slim

COPY --from=builder /opt/venv /opt/venv

WORKDIR /github/workspace/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        pandoc \
        tree

ENV PATH="/opt/venv/bin:$PATH"

ADD tasks.py /github/workspace/
RUN chmod +x tasks.py && \
    pwd && \
    ls -lA
ENTRYPOINT [ "python", "/github/workspace/tasks.py" ]
