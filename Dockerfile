FROM python:3.10
# by this command we tell docker to not create file with .pyc
ENV PYTHONDONTWRITEBYTECODE 1 
 # by this command we tell docker to not add anything from docker to terminal so that we see terminal as we  saw before. 
ENV PYTHONUNBUFFERED 1  
WORKDIR /code
# copy everythong from requierment.txt to our workdir
COPY requirements.txt /code/
# then we install everything from it to our workdir
RUN  pip install -r requirements.txt   
#copy all of this project to the workdir
COPY . /code/
