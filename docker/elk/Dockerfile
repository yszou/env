FROM java
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD logstash.conf /root/logstash.conf
ADD supervisord.conf /root/supervisord.conf
ADD nginx.conf /root/nginx.conf

ADD elasticsearch-1.3.2.tar.gz /opt
ADD logstash-1.4.2.tar.gz /opt
ADD kibana-3.1.0.tar.gz /opt
ADD nginx-1.6.2.tar.gz /root/src

#RUN apt-get update -y && \
#    apt-get upgrade -y

RUN pip install -i http://pypi.douban.com/simple/ supervisor
RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q
RUN cd /root/src/nginx-1.6.2 && \
    ./configure --prefix=/opt/nginx --without-http_rewrite_module && \
    make && \
    make install


CMD ["bash", "/root/run"]
