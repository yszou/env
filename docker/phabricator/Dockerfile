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
    php5-fpm \
    sendmail

RUN sed -i 's/; process.max = 128/process.max = 1/' /etc/php5/fpm/php-fpm.conf && \
    sed -i 's/;listen.mode = 0660/listen.mode = 0666/' /etc/php5/fpm/pool.d/www.conf && \
    sed -i 's/pm = dynamic/pm = static/' /etc/php5/fpm/pool.d/www.conf && \
    sed -i 's/pm.max_children = 5/pm.max_children = 3/' /etc/php5/fpm/pool.d/www.conf

RUN apt-get install -y mysql-server && \
    service mysql start && \
    sleep 5 && \
    /var/www/phabricator/bin/storage upgrade -f && \
    /var/www/phabricator/bin/config set phabricator.base-uri 'http://182.92.218.33:8080/'

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
