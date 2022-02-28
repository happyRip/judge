FROM cicirello/pyaction:latest as builder

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


FROM cicirello/pyaction:latest

COPY --from=builder /opt/venv /opt/venv

WORKDIR /github/workspace/

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        # git \
        pandoc

ENV PATH="/opt/venv/bin:$PATH"

COPY . .
ENTRYPOINT [ "python", "tasks.py" ]
