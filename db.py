#mysql 모듈 임포트
import pymysql

def get_connection():
    conn = pymysql.connect(host="127.0.0.1",user='root',password='1234',db='sample1',charset='utf8')
    if conn:
        print('디비접속 완료')
        print(conn)
    return conn
# 연결 테스트 함수 호출
conn=get_connection()
# print(conn)
cursor = conn.cursor()
# print(cursor)
sql = '''
    select * from worldcity;
'''
cursor.execute(sql)
result = cursor.fetchall()
print(result[-1])
print(type(result))
num = []
code=[]
country=[]
for i in result:
    print(i)
    num.append(i[0])
    code.append(i[1])
    country.append(i[2])
print(num,code,country)
sql = '''
    select * from worldcity limit 10;
'''
cursor.execute(sql)
result2=cursor.fetchall()
print(len(result2))
temp_list =[]
for row in result2:
    temp_dic = {}
    temp_dic['No']=row[0]
    temp_dic['Code']=row[1]
    temp_dic['Name']=row[2]
    temp_dic['GNP']=row[3]
    temp_dic['Population']=row[4]
    temp_list.append(temp_dic)
print(temp_list)

for row in temp_list:
    for key in row:
        print(key,'=>',row[key])
    print('-'*20)
