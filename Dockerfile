# Use an official Python runtime as a parent image
FROM python:3.8.18

# # Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0
# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code/
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
