FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD rabbitmq-server-generic-unix-3.3.5.tar.gz /root/src

RUN apt-get update -y && \
    apt-get install -y erlang
RUN cp /root/src/rabbitmq_server-3.3.5/etc/rabbitmq/rabbitmq.config.example \
       /root/src/rabbitmq_server-3.3.5/etc/rabbitmq/rabbitmq.config && \
    sed -i 's/%% {loopback_users, \[\]},/{loopback_users, \[\]}/' /root/src/rabbitmq_server-3.3.5/etc/rabbitmq/rabbitmq.config

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
