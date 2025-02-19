FROM python:3.9-slim

COPY . /home/dt-server
WORKDIR /home/dt-server

COPY ./requirements.txt /home/dt-server/requirements.txt

RUN apt-get update
RUN pip install -r requirements.txt

CMD ["python","main.py"]