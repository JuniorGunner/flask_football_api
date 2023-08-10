FROM python:3.9-slim

WORKDIR /santex_test

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# ENV PYTHONPATH /santex_test:$PYTHONPATH

COPY . .

CMD ["python", "run.py"]
