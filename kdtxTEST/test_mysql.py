import pymysql

conn = None
cursor = None

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, database="python", charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from students")
    result = cursor.fetchone()
    cursor.rownumber = 0
    result2 = cursor.fetchmany(3)
    cursor.rownumber = 0
    re = cursor.fetchall()
    print(result)
    print(result2)
    print(re)
except Exception as err:
    print("数据库查询出错", str(err))

finally:
    cursor.close()
    conn.close()
