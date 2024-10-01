FROM python:alpine3.16
RUN apk add busybox-initscripts openrc mariadb-client --no-cache
RUN pip install schedule
WORKDIR /app
COPY main.py /app/main.py
#iniciar o script python a partir do venv
CMD ["python3", "-u" ,"./main.py"]