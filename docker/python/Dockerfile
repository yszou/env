FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD requirements /root/requirements

RUN apt-get update && \
    apt-get upgrade -y

RUN pip install -vv -i http://mirrors.aliyun.com/pypi/simple/ -r /root/requirements

RUN rm -rf ~/.ssh/id_rsa && \
    rm -rf ~/.ssh/id_rsa.pub && \
    ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' -q

CMD ["bash", "/root/run"]

