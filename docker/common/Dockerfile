FROM ubuntu:18.04
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
#ADD sources.list /etc/apt/sources.list
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
    libpython3-dev \
    python3-dev \
    python3-pip \
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
    dpkg-dev \
    net-tools

#RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com pip --upgrade
#RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com \
RUN pip3 install pip --upgrade
RUN pip3 install \
    pillow \
    lxml \
    psycopg2-binary \
    tornado \
    sqlalchemy \
    pygments \
    cffi \
    pycrypto \
    #ansible \
    xlrd \
    xlwt \
    qrcode


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


RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]

