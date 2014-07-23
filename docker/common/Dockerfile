FROM ubuntu:14.04
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD sources.list /etc/apt/sources.list
ADD id_rsa.pub /tmp/pubkey
ADD locale /etc/default/locale
ADD requirements /root/requirements

RUN mkdir -p /root/.ssh && \
    cat /tmp/pubkey >> /root/.ssh/authorized_keys && \
    rm -rf /tmp/pubkey

RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir -p /var/run/sshd && \
    sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

RUN apt-get install -y \
    language-pack-en-base \
    language-pack-zh-hans \
    man \
    gcc \
    g++ \
    zlib1g-dev \
    libjpeg-dev \
    libopenjpeg-dev \
    libpng12-dev \
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
    sqlite3 \
    postgresql-client \
    mysql-client \
    axel \
    ctags \
    zsh \
    locate

RUN rm -rf /usr/bin/python && \
    ln -s /usr/bin/python2.7 /usr/bin/python

#RUN pip install -vv -i http://pypi.douban.com/simple/ -r /root/requirements
RUN pip install -vv -i http://pypi.hustunique.com/simple/ -r /root/requirements

ENV HOME /root
RUN mkdir -p /root/volumn

RUN mkdir -p /root/src && \
    mkdir -p /root/src/github && \
    cd /root/src/github && \
    git clone https://github.com/zephyrzou/env.git && \
    cd /root/src/github/env/vim && \
    bash install && \
    cd /root/src/github/env/zsh && \
    bash install

RUN sed -i 's/\/root:\/bin\/bash/\/root:\/bin\/zsh/' /etc/passwd

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
