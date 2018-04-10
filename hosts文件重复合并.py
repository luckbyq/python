#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,os,re,time,datetime

#用来备份当前的hosts文件。
nowday = datetime.datetime.now().strftime('%Y-%m-%d')
nowTime = datetime.datetime.now().strftime('%H:%M:%S')
os.system('mkdir -p /backup/hosts/%s' % nowday)
os.system('cp /etc/hosts /backup/hosts/%s/hosts_%s' % (nowday,nowTime))

#判断传值是否存在。
try:
    oldfile = sys.argv[1]
    newfile = sys.argv[2]
except:
    print "cmd is   python  xxxx.py <oldfile path> <newfile path>"
    exit(1)

#清空列表中的空字符模块。
def sp(l):
    if '' in l:
        for i in range(l.count('')):
            l.remove('')

#主工作模块。
def add(oldfile,newfile):
    print "Being merged......"
    #睡眠1秒，保证hosts文件备份不会被覆盖。
    time.sleep(1)
    #初始化新的hosts文件
    os.system('rm -f %s' % newfile)
    os.system('touch %s' % newfile)
    #遍历老文件，查看新文件。如果新文件不存在则写入，如果存在则追加。
    for i in open(oldfile,'r').readlines():
        l = []
        l = re.split(' +|\t|\n|', i.strip())
        sp(l)
        ip = l[0]
        new = open(newfile,'a+')
        for I in new.readlines():
            if ip in I:
                L = []
                L = re.split(' +|\t|\n|', I.strip())
                sp(L)
                l.remove(ip)
                L = L + l
                L = '\t'.join(L)
                os.system("sed -i 's/%s.*/%s/g' %s" % (ip,L,newfile))
        new.writelines('\t'.join(l)+'\n')
        new.close()
    print "Merged success!!"
add(oldfile,newfile)