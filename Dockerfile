FROM alpine:3.1
RUN apk add --update python py-pip
RUN pip install Flask
RUN pip install -r requirments.txt
COPY . /app
EXPOSE  5000
CMD ["python", "/app/app.py", "-p 5000"]
