#mysql 모듈 임포트
import pymysql

def get_connection():
    conn = pymysql.connect(host="127.0.0.1",user='root',password='1234',db='sample2',charset='utf8')
    if conn:
        print('디비접속 완료')
        print(conn)
    return conn
def get_emp_list():
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    # print(cursor)
    #no 기준으로 내림차순 정렬
    sql = '''
        select * from emp order by no desc;
    '''
    cursor.execute(sql)
    result2 = cursor.fetchall()

    temp_list =[]
#딕셔너리화

    for row in result2:
        temp_dic = {}
        temp_dic['No']=row[0]
        temp_dic['first_name']=row[1]
        temp_dic['last_name']=row[2]
        temp_dic['gender']=row[3]
        temp_dic['birth']=row[4]
        temp_list.append(temp_dic)
    conn.close()
    print("db연결 종료")
    return temp_list
def get_empone_list(no):
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    # print(cursor)
    #no 기준으로 내림차순 정렬
    sql = '''
        select * from emp where no=%s;
    '''
    cursor.execute(sql,no)
    result2 = cursor.fetchone()


#딕셔너리화


    temp_dic = {}
    temp_dic['No']=result2[0]
    temp_dic['first_name']=result2[1]
    temp_dic['last_name']=result2[2]
    temp_dic['gender']=result2[3]
    temp_dic['birth']=result2[4]
    conn.close()
    print("db연결 종료")
    return temp_dic
def emp_add(c_first_name,c_last_name,c_gender,c_birth):
    # 연결 테스트 함수 호출
    conn=get_connection()
    # print(conn)
    cursor = conn.cursor()
    # print(cursor)
    #no 기준으로 내림차순 정렬
    sql = '''
        insert into emp (first_name,last_name,gender,birth) values(%s,%s,%s,%s);
    '''
    cursor.execute(sql,(c_first_name,c_last_name,c_gender,c_birth))
    conn.commit()
    conn.close()
    print("db연결 종료")
# print(get_country_list())
def emp_delete(no):
    conn=get_connection()
    cusor=conn.cursor()
    sql = '''
        delete from emp where no=%s
    '''
    cusor.execute(sql,no)
    conn.commit()
    conn.close()
    print("db연결 종료")

def emp_update(c_no,c_first_name,c_last_name, c_gender, c_birth):
    # 데이타베이스 접속함수 호출
    conn = get_connection()
    # 작업변수 생성
    cursor = conn.cursor()

    # 레코드 수정 sql 구문 
    sql = '''
            update emp
                set 
                    first_name=%s,
                    last_name=%s,
                    gender=%s,
                    birth=%s
                where No=%s
            '''

    cursor.execute(sql, (c_first_name, c_last_name,c_gender,c_birth, c_no))
    conn.commit()
    conn.close()