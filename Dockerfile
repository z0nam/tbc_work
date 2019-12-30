FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -U otree
COPY . /home/coopedu/
WORKDIR /home/coopedu
EXPOSE 8000
CMD otree devserver
