FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y openjdk-7-jdk

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]
