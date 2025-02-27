#choosing base image
FROM python:3.11-alpine

#setting environment variable
ENV PYTHONDONTWRITEBYTCODE=1
ENV PYTHONUBUFFERED=1

#set working directories inside container
WORKDIR /app

#Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#copy project sourcecode 

COPY . /app/

#expose port on container

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



