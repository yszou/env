FROM java
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD logstash.conf /root/logstach.conf

ADD elasticsearch-1.3.2.tar.gz /opt
ADD logstash-1.4.2.tar.gz /opt
ADD kibana-3.1.0.tar.gz /opt

RUN apt-get update -y && \
    apt-get upgrade -y
RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
