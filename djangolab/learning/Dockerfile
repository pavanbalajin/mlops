# base image  
FROM python:3.8.3-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
#docker run -it -p 8000:8000 django
#docker build -t django .  