FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD node-v0.10.31.tar.gz /root/src
ADD outbound /root/src/outbound

RUN apt-get upgrade -y
RUN cd /root/src/node-v0.10.31 && \
    ./configure && \
    make && \
    make install && \
    npm install -g Haraka


RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
