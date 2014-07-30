#! /usr/bin/python
# -*- coding: utf-8 -*-

import random

s = ''
while True:
    c = chr(random.randint(33, 126))
    if c in ['"', "'", '$', '|', '/', '\\']:
        continue
    else:
        s += c
        if len(s) == 32: 
            break
print s
