FROM python:3.9-slim

WORKDIR /santex_test

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]


# FROM python:3.9-slim

# WORKDIR /my_flask_app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000"]
