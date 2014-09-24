FROM web
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD requirements /root/requirements
RUN pip install -vv -r /root/requirements --proxy http://10.1.190.164:8080


RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
