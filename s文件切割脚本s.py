#这个脚本是当时用来分割文件的，按大小分割
# -*- coding: utf-8 -*-
import os
import time

#这个函数是定义了一个单位的换算
#def formatsize(bytes):
#    try:
#        bytes = float(bytes)
#        kb = bytes / 1024
#    except:
#        print "input file format err"
#        return "Error"
#    if kb >= 1024:
#        M = kb / 1024
#        if M > 1024:
#            G = M / 1024
#            return "%fG" % (G)
#        else:
#            return "%fM" % (M)
#    else:
#        return "%fkb" % (kb)


#这里定义了获取文件大小的方法
def getfilesize(path):
    try:
        size = os.path.getsize(path)
#        return formatsize(size)
        return size
    except Exception as err:
        print err

path = "/home/www/dazuizhibo1/sys/fun/logs/201707/sql.txt"
#getfilesize(path)


#这里定义了切割方法，调用获取文件大小的方法
def movefiles(filename):
    aa = getfilesize(filename)
#    cc = int(aa)
    if aa >= 104857600:     #这里是大于100M
        bb = time.time()    #这里是生成一个当前的时间戳
        cc = str(bb)        #将这个时间戳的类型转换一下
        os.rename(path, path+cc)   #然后拼接起来，作为切割后的新文件的文件名


movefiles(path)