#这个脚本是备份数据库，我这里是获取了mysql数据目录，然后循环去备份特定的数据库

import os
import re
import time

db_user = 'root'
db_passwd = "'sss'"    #这里在linux中明文密码，mysql报错了。所以将他用双引号再加单引号引起来
backdir = '/tmp/jiange/'
def file(path):
    aa = os.listdir(path)  #这里是获取这个路径下的所有文件
    for db in aa:
        if db.startswith("z_"):   #这里是判断字符串开头，startswith（）
            #这里是字符串拼接，然后赋值了变量
            dumpcmd = '/home/local/mysql/bin/mysqldump -h' + db_host + ' -u' + db_user + ' -p' + db_passwd + ' --skip-lock-tables' + ' ' + db + ' ' + '>' + backdir + db + '.sql'
            #执行系统命令
            os.system(dumpcmd)
            time.sleep(1)
        elif db.startswith("r_"):
            dumpcmd = '/home/local/mysql/bin/mysqldump -h' + db_host + ' -u' + db_user + ' -p' + db_passwd + ' --skip-lock-tables' + ' ' + db + ' ' + '>' + backdir + db + '.sql'
            os.system(dumpcmd)
            time.sleep(1)


path = "/home/local/mysql/var"

file(path)