#오라클DB 연동
import cx_Oracle

# 데이터소스 네임 객체 생성(접속주소, 포트번호, 서비스명)
dsn = cx_Oracle.makedsn('localhost', 1521, service_name = 'orcl')
# DB연결객체 
conn = cx_Oracle.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'UTF-8')

cur = conn.cursor() #커서생성
query = 'SELECT * FROM EMP'

for row in cur.execute(query):
    print(row)

cur.close()
conn.close()