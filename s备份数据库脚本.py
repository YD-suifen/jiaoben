#����ű��Ǳ������ݿ⣬�������ǻ�ȡ��mysql����Ŀ¼��Ȼ��ѭ��ȥ�����ض������ݿ�

import os
import re
import time

db_user = 'root'
db_passwd = "'sss'"    #������linux���������룬mysql�����ˡ����Խ�����˫�����ټӵ�����������
backdir = '/tmp/jiange/'
def file(path):
    aa = os.listdir(path)  #�����ǻ�ȡ���·���µ������ļ�
    for db in aa:
        if db.startswith("z_"):   #�������ж��ַ�����ͷ��startswith����
            #�������ַ���ƴ�ӣ�Ȼ��ֵ�˱���
            dumpcmd = '/home/local/mysql/bin/mysqldump -h' + db_host + ' -u' + db_user + ' -p' + db_passwd + ' --skip-lock-tables' + ' ' + db + ' ' + '>' + backdir + db + '.sql'
            #ִ��ϵͳ����
            os.system(dumpcmd)
            time.sleep(1)
        elif db.startswith("r_"):
            dumpcmd = '/home/local/mysql/bin/mysqldump -h' + db_host + ' -u' + db_user + ' -p' + db_passwd + ' --skip-lock-tables' + ' ' + db + ' ' + '>' + backdir + db + '.sql'
            os.system(dumpcmd)
            time.sleep(1)


path = "/home/local/mysql/var"

file(path)