FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD memcached-1.4.20.tar.gz /root/src

RUN apt-get upgrade -y
RUN apt-get install -y libevent1-dev

RUN cd /root/src/memcached-1.4.20 && \
    ./configure --prefix=/opt/memcached --enable-64bit && \
    make && \
    make install

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
