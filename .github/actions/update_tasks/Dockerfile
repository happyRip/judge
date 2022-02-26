FROM python:3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pwd
RUN ls -A
ENTRYPOINT [ "python", "tasks.py" ]