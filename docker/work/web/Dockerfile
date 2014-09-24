FROM python
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD nginx-1.6.2.tar.gz /root/src

RUN apt-get upgrade -y
RUN apt-get install -y libpcre3-dev
RUN cd /root/src/nginx-1.6.2 && \
    ./configure --prefix=/opt/nginx --with-http_ssl_module && \
    make && \
    make install

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
