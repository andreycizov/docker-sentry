FROM dockerfile/python

RUN apt-get update && apt-get install -y \
    postgresql-client-common \
    libpq-dev \
    mysql-client \
    libmysqlclient-dev

RUN pip install MySQL-python psycopg2 sentry redis==2.8.0 

EXPOSE 80
ADD sentry.conf.py /sentry.conf.py

ENTRYPOINT ["/usr/local/bin/sentry", "--config=/sentry.conf.py"]
CMD ["start"]
