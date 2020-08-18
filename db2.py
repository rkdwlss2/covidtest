#mysql 모듈 임포트
import pymysql

def get_connection():
    conn = pymysql.connect(host="127.0.0.1",user='root',password='1234',db='sample1',charset='utf8')
    if conn:
        print('디비접속 완료')
        print(conn)
    return conn
def get_country_list():
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    # print(cursor)
    #no 기준으로 내림차순 정렬
    sql = '''
        select * from worldcity order by no desc;
    '''
    cursor.execute(sql)
    result2 = cursor.fetchall()

    temp_list =[]
#딕셔너리화

    for row in result2:
        temp_dic = {}
        temp_dic['No']=row[0]
        temp_dic['Code']=row[1]
        temp_dic['Name']=row[2]
        temp_dic['GNP']=row[3]
        temp_dic['Population']=row[4]
        temp_list.append(temp_dic)
    conn.close()
    print("db연결 종료")
    return temp_list

def country(no):
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    # print(cursor)
    sql = '''
        select * from worldcity where no=%s;
    '''
    cursor.execute(sql,no)
    result = cursor.fetchone()
    temp_dic = {}
    temp_dic['No']=result[0]
    temp_dic['Code']=result[1]
    temp_dic['Name']=result[2]
    temp_dic['GNP']=result[3]
    temp_dic['Population']=result[4]
    conn.close()
    print("db연결 종료")
    return temp_dic

# print(country(1))


#특정 단어가 들어가는 레코드 검색 sql 구문
#select * from worldcity where name like "a%";

def search_country_list(name):
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    # print(cursor)
    sql = '''
        select * from worldcity where name like %s;
    '''
    name='%'+name+'%'
    cursor.execute(sql,name)
    result = cursor.fetchall()
    temp_list =[]
#딕셔너리화
    for row in result:
        temp_dic = {}
        temp_dic['No']=row[0]
        temp_dic['Code']=row[1]
        temp_dic['Name']=row[2]
        temp_dic['GNP']=row[3]
        temp_dic['Population']=row[4]
        temp_list.append(temp_dic)
    conn.close()
    print("db연결 종료")
    return temp_list

#레코드 추가함수
def country_add(c_code,c_name,c_ngp,c_population):
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    sql='''
        insert into worldcity (code,name,gnp,population) values(%s,%s,%s,%s)
    '''
    cursor.execute(sql,(c_code,c_name,c_ngp,c_population))
    #db에 반영을 해줘야해서 conn.commit()필수 return 필요 없음 넣는거기 때문에
    conn.commit()
    conn.close()

def country_delete(country_no):
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    sql='''
        delete from worldcity where no = %s
    '''
    cursor.execute(sql,(country_no))
    conn.commit()
    conn.close()
# print(search_country_list('kor'))
# print(get_country_list())

def country_update(c_no, c_gnp, c_population):
    # 데이타베이스 접속함수 호출
    conn = get_connection()
    # 작업변수 생성
    cursor = conn.cursor()

    # 레코드 수정 sql 구문 
    sql = '''
            update worldcity
                set 
                    GNP=%s,
                    Population=%s
                where No=%s
            '''

    cursor.execute(sql, (c_gnp, c_population, c_no))
    conn.commit()
    conn.close()