import pymysql
import random
def create_id():
    L = []
    for i in range(5):
        Le= random.sample(range(1, 271), 90)  # 生成学号
        L.append(Le)
    return L

def create_name():  # 随机生成姓名
    nam =[]
    for i in range(5):
        na = []
        first_name = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱",
                      "秦", "尤",
                      "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻",
                      "柏", "水",
                      "窦", "章", "云", "苏", "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花",
                      "方"]
        second_name = ["静", "霞", "雪", "思", "平", "东", "志宏", "峰", "磊", "雷", "文", "明浩", "光", "超", "军", "达",
                       "伟", "华", "建国",
                       "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "风", "博凯", "徐坤", "震",
                       "倩倩", "鹏", "均", "达智", "欣欣", "易鹏", "蕾蕾"]
        for j in range(90):
            name = random.choice(first_name) + random.choice(second_name)
            na.append(name)
        nam.append(na)
    return nam

def create_table():
    c = [[0] * 20 for _ in range(90)]     # c[i]为第i位同学的出勤情况，1代表缺勤，0代表出勤
    absentNum = random.randint(5, 8)   # 经常缺席人数
    absent_ord = random.sample(range(90), absentNum)   # 经常缺席的学生序号
    temp = list(range(90))
    for i in absent_ord:
        temp.remove(i)  # 剔除经常缺席学生序号
        absenttime = random.sample(range(20), 16)
        for j in absenttime:
            c[i][j] = 1  # 标记经常缺席的学生缺席课次
    for i in range(20):  # 第i节课
        a = random.randint(0, 3)  # 缺席人数（偶尔）
        absentCal = random.sample(temp, a)  # 缺席学生学号
        for j in absentCal:
            c[j][i] = 1
    return c

# 连接数据库
conn = pymysql.connect(host="localhost", user="root",\
                       password="123456",cursorclass=pymysql.cursors.DictCursor)
try:
    # 创建游标
    cur = conn.cursor()
    # 执行sql查询语句
    cur.execute("CREATE DATABASE IF NOT EXISTS DS;")
    cur.execute("USE DS;")
    ids = create_id()
    names = create_name()
    for i in range(5):
        cur.execute("DROP TABLE if EXISTS course_" + str(i) + ";")
        cur.execute("CREATE table course_"+str(i)+"(serialNum int primary key,"
                    "stuName varchar(20),stu_id int,absentNum int default 0);")
        for j in range(90):
            cur.execute("INSERT INTO course_"+str(i)+"(serialNum,stuName,stu_id)\
                          VALUES ("+str(j)+",'"+names[i][j]+"',"+str(ids[i][j])+");")
        cur.execute("drop view if exists temp")
        cur.execute("create view temp as select serialNum from course_" + str(i) + " where absentNum >=0")
        cur.execute("select * from course_"+str(i)+" where absentNum >=0")
        result = cur.fetchall()
        for j in range(len(result)):
            print(result[j])
            sql = "update course_" + str(i) + " set absentNum=absentNum+1\
                     where serialNum in (select * from temp);"
            cur.execute(sql)
    cur.close()
    # 关闭数据库连接
    conn.close()
except pymysql.err.MySQLError as _error:
    print('操作失败')
    raise _error