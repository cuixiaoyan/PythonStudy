#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("47.100.236.144", "root", "root", "python")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM user")

# 使用 fetchall() 方法获取s所有数据.
data = cursor.fetchall()

print(data)

# 关闭数据库连接
db.close()

