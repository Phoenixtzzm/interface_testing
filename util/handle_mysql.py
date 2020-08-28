# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/28 1:36'
import sys,os
sys.path.append(os.pardir)
import pymysql


# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='tanz',
    charset='utf8'
)

# 获取游标,才能操作数据
cursor = connect.cursor()
a= cursor.execute("update student set sage=100 where sname='谈政'")
# sql =  'insert into student values (%s,%s,%s,%s)'
# b =cursor.execute(sql,(7,'测试',23,'男'))
# 一次执行完毕
# cursor.executemany()
#回滚事务
# conn.rollback()

aa = cursor.fetchmany(2)
print(aa)
cursor.close()
connect.commit()

connect.close()








