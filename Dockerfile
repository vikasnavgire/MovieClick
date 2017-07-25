FROM ubuntu:latest
MAINTAINER Vikas Navgire "viki.81188@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libmysqlclient-dev
RUN pip install --upgrade pip
COPY . /app
RUN pip install -r /app/requirments.txt
ENTRYPOINT ["python"]
CMD ["/app/app.py"]
