#����ű��ǵ�ʱ�����ָ��ļ��ģ�����С�ָ�
# -*- coding: utf-8 -*-
import os
import time

#��������Ƕ�����һ����λ�Ļ���
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


#���ﶨ���˻�ȡ�ļ���С�ķ���
def getfilesize(path):
    try:
        size = os.path.getsize(path)
#        return formatsize(size)
        return size
    except Exception as err:
        print err

path = "/home/www/dazuizhibo1/sys/fun/logs/201707/sql.txt"
#getfilesize(path)


#���ﶨ�����и�������û�ȡ�ļ���С�ķ���
def movefiles(filename):
    aa = getfilesize(filename)
#    cc = int(aa)
    if aa >= 104857600:     #�����Ǵ���100M
        bb = time.time()    #����������һ����ǰ��ʱ���
        cc = str(bb)        #�����ʱ���������ת��һ��
        os.rename(path, path+cc)   #Ȼ��ƴ����������Ϊ�и������ļ����ļ���


movefiles(path)