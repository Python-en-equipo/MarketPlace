FROM python:3.8

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


WORKDIR /app
COPY . ./app
# Install pip requirements 
#COPY backend/requirements.txt /backend/
#RUN python -m pip install --upgrade pip
#RUN python -m pip install -r requirements.txt
#RUN python manage.py makemigrations
#RUN python manage.py migrate



CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]