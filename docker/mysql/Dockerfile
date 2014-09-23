FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD mysql-5.6.20.zip /root/src/mysql-5.6.20.zip
ADD my.cnf /root/my.cnf

#RUN apt-get upgrade -y
RUN apt-get install -y \
    unzip \
    cmake \
    libncurses5-dev

RUN cd /root/src/ && \
    unzip mysql-5.6.20.zip && \
    cd mysql-5.6.20 && \
    cmake . && \
    make && \
    make install

RUN mkdir /usr/share/mysql && \
    mkdir /var/log/mysql && \
    cp /root/src/mysql-5.6.20/sql/share/english/errmsg.sys /usr/share/mysql/errmsg.sys && \
    rm -rf /usr/local/mysql/my.cnf && \
    mv /root/my.cnf /usr/local/mysql/my.cnf && \
    groupadd mysql && \
    useradd -r -g mysql mysql && \
    cd /usr/local/mysql && \
    chown -R mysql . && \
    chgrp -R mysql . && \
    scripts/mysql_install_db --user=mysql --basedir=/usr/local/mysql && \
    chown -R root . && \
    chown -R mysql data && \
    cp support-files/mysql.server /etc/init.d/mysql.server && \
    ln /usr/local/mysql/bin/mysqld_safe /usr/bin/mysqld_safe


RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
