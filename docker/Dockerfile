FROM ubuntu:20.04

RUN apt-get update -y && \
	apt-get install -y sqlite3 && \
	apt-get install -y python3 && \
	apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY src src/
COPY start.sh .

RUN chmod +x ./start.sh

CMD ["./start.sh"]