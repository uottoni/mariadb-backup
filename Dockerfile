FROM python:alpine3.16
#RUN apt-get update && apt-get -y install cron vim
RUN apk add busybox-initscripts openrc --no-cache
RUN pip install schedule
WORKDIR /app
#COPY crontab /etc/cron.d/crontab
COPY main.py /app/main.py
#RUN chmod 0644 /etc/cron.d/crontab

#CMD ["/usr/bin/cron", "-l", "2" ,"-f", "/etc/cron.d/crontab"]
#iniciar o script python a partir do venv
#CMD ["/bin/sh", "-c", "source .venv/scripts/activate && python3 -u ./zabbix_os_sinal.py"]
CMD ["python3", "-u" ,"./main.py"]