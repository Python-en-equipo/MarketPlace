FROM python:3.8

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements 
#COPY backend/requirements.txt /backend/
#RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . ./app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]