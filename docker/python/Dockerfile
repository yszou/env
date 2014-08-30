FROM common
MAINTAINER YS.Zou <yeshengzou@gmail.com>

ADD run /root/run
ADD requirements /root/requirements

RUN pip install -vv -i http://pypi.douban.com/simple/ -r /root/requirements

CMD ["bash", "/root/run"]
