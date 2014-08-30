FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD postgresql-9.3.4.tar.gz /root/src

RUN cd /root/src/postgresql-9.3.4 && \
    ./configure --prefix=/opt/postgresql --with-openssl --with-python && \
    make && \
    make install

RUN groupadd postgres && \
    useradd -m -g postgres postgres && \
    cd /opt/postgresql/bin && \
    su postgres -c "./initdb -U root /home/postgres/pg_data" && \
    echo "host all test 0.0.0.0/0 trust" >> /home/postgres/pg_data/pg_hba.conf && \
    echo "listen_addresses = '*'" >> /home/postgres/pg_data/postgresql.conf && \
    su postgres -c "/opt/postgresql/bin/pg_ctl -D /home/postgres/pg_data -l /home/postgres/pg_log start" && \
    sleep 3 && \
    /opt/postgresql/bin/createuser -d test && \
    /opt/postgresql/bin/createdb -O test test && \
    sleep 2 && \
    su postgres -c "/opt/postgresql/bin/pg_ctl -D /home/postgres/pg_data -l /home/postgres/pg_log stop"

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
