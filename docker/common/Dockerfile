FROM ubuntu:18.04
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD sources.list /etc/apt/sources.list
ADD id_rsa.pub /tmp/pubkey
ADD locale /etc/default/locale

RUN mkdir -p /root/.ssh && \
    cat /tmp/pubkey >> /root/.ssh/authorized_keys && \
    rm -rf /tmp/pubkey

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y openssh-server && \
    mkdir -p /var/run/sshd && \
    sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

RUN apt-get install -y \
    language-pack-en-base \
    language-pack-zh-hans \
    man \
    sudo \
    gcc \
    g++ \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    libgif-dev \
    libfreetype6-dev \
    libtiff-dev \
    libwebp-dev \
    libxml2-dev \
    libxslt1-dev \
    libsqlite3-dev \
    libmysqlclient-dev \
    libpq-dev \
    libyaml-dev \
    libffi-dev \
    libreadline6-dev \
    python2.7 \
    python-dev \
    python-pip \
    vim \
    git \
    curl \
    wget \
    sqlite3 \
    postgresql-client \
    mysql-client \
    axel \
    ctags \
    zsh \
    locate \
    telnet \
    dnsutils \
    libmemcached-dev \
    libpcre3-dev \
    libevent1-dev \
    unzip \
    cmake \
    libncurses5-dev \
    dpkg-dev


RUN rm -rf /usr/bin/python && \
    ln -s /usr/bin/python2.7 /usr/bin/python

ENV HOME /root
RUN mkdir -p /root/volumn

RUN mkdir -p /root/src && \
    mkdir -p /root/src/github && \
    cd /root/src/github && \
    git clone https://github.com/yszou/env.git && \
    cd /root/src/github/env/vim && \
    bash install && \
    cd /root/src/github/env/zsh && \
    bash install

RUN sed -i 's/\/root:\/bin\/bash/\/root:\/bin\/zsh/' /etc/passwd

#RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]

