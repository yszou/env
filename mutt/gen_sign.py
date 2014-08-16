# -*- coding: utf-8 -*-

from os import chdir
from glob import glob
from random import shuffle

chdir("/home/zys/github/zephyrzou.github.io/source")
l = glob("*.t2t")
shuffle(l)
fn = l[0]
with open(fn,  "r") as f: h = f.readline().strip()
s = "%s: %s" % (h, "http://www.zouyesheng.com/" + fn.split(".", 1)[0] + ".html" + "\n\n")
with open("/home/zys/.signature", "r") as f: sign = f.read()
with open("/tmp/signature", "w") as f: f.write(sign + "\n" + s)
print "/tmp/signature"
