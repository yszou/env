FROM python3
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD nginx-1.14.0.tar.gz /root/src

RUN apt-get update && \
    apt-get upgrade -y

RUN cd /root/src/nginx-1.14.0 && \
    ./configure --prefix=/opt/nginx --with-stream && \
    make && \
    make install

RUN useradd -m app

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]

