FROM tiangolo/uwsgi-nginx-flask:python3.6
ENV LISTEN_PORT 5000

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
