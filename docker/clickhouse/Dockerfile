FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD clickhouse.list /etc/apt/sources.list.d/clickhouse.list

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y --force-yes clickhouse-client clickhouse-server-common


RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]

