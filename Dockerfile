FROM python:3.5
ENV PYTHONUNBUFFERED 1
#ENV FLASK_APP main.py
ENV FLASK_ENV=development
RUN apt-get update && apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]