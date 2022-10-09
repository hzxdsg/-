import pymysql
# 连接数据库
conn = pymysql.connect(host="localhost", user="root", password="123456",
                       cursorclass=pymysql.cursors.DictCursor)
try:
    # 创建游标
    cur = conn.cursor()
    # 执行sql查询语句
    cur.execute("CREATE DATABASE DS IF NOT EXISTS DS;")
    cur.execute("USE DS;")
    cur.execute("CREATE table if not EXISTS create table /"
                "course(c_id int primary key,s_id varchar(9) ,/"
                "stuName varchar(12),/"
                "absentNumber int default 0);")
    # 关闭游标

    cur.close()
    # 关闭数据库连接
    conn.close()
except pymysql.err.MySQLError as _error:
    print('操作失败')
    raise _error