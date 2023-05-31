FROM python:3.8 AS Builder

WORKDIR /DOBIZ

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /DOBIZ

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]