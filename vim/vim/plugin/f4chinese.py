#! /usr/bin/python
# -*- coding: UTF-8 -*-

'''
配合f4chinese.vim使用的功能实现.
这个程序会根据码表,查询某输入在指定字符串中的匹配位置.
如,对于五笔的码表,对于如下字符串(不包括前置空格):
    展示了几项让实体世界和数字世界互动的工具
'nf' 的输入,结果返回0 ('展示')
'pw' 的输入,结果返回6 ('实体')
'''

import sys

TABLE_ENCODING = 'utf8' #码表的编码
INPUT_ENCODING = 'utf8' #输入字符串编码

def f4chinese(table, line, firstChars):
    '''
    在line中,查找firstChars
    table是备查码表
    返回查找到的字符的位置,没找到返回-1
    '''

    #解析码表,得到一个dict
    file = open(table)
    dict = {}
    map(lambda x: dict.__setitem__(x.split(' ')[0].decode(TABLE_ENCODING),
                                   map(lambda u: u.strip(), x.split(' ')[1:])),
        file.readlines())

    lineList = list(line.decode(INPUT_ENCODING))
    charList = list(firstChars.decode(INPUT_ENCODING))

    flag = 0 
    r = 0
    for char in lineList:
        r += 1

        #line中的某个字符可能在码表中没有, 如空格,标点
        try:
            t = dict[char]
        except KeyError:
            t = []

        if charList[flag] in t:
            flag += 1
        elif charList[0] in t: 
             #为1的情况,在不然对于 每个公式mggs 查gs会出问题
            flag = 1
        else:
            flag = 0

        if flag == len(charList):
            break

    if flag == 0:
        return -1
    else:
        return r - flag

if __name__ == '__main__':
    r = f4chinese(sys.argv[1], sys.argv[2], sys.argv[3])
    if r < 0:
        sys.exit()
    else:
        #用print会多出一个换行,麻烦
        #r==0时的情况要处理一下
        sys.stdout.write('\<Right>' * r or '\<Esc>')

