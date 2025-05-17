FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3

#needed for flask server
RUN apt-get install -y python3-pip

RUN pip install flask==3.0.*
WORKDIR /home/ubuntu

COPY backend.py /home/ubuntu

EXPOSE 5000

# This will ensure this file is used in the setup for the Flask app by including the 
#ENV FLASK_APP=backend

CMD ["python3", "backend.py"]
#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]


