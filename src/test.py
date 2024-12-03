import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='talaton123',
    database='benhvien',
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        print("Connected to database:", result)
finally:
    connection.close()
