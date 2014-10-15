FROM web
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD nginx.conf /opt/nginx/conf/nginx.conf

RUN mkdir /var/www && \
    chown www-data:www-data /var/www

RUN mkdir /var/repo && \
    chown www-data:www-data /var/repo

ADD libphutil.tar.gz /var/www
ADD arcanist.tar.gz /var/www
ADD phabricator.tar.gz /var/www

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y \
    dpkg-dev \
    php5-mysql \
    php5-gd \
    php5-dev \
    php5-curl \
    php-apc \
    php5-cli \
    php5-json \
    php5-fpm

RUN apt-get install -y mysql-server && \
    service mysql start && \
    sleep 5 && \
    /var/www/phabricator/bin/storage upgrade -f

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
