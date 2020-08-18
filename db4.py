#mysql 모듈 임포트
import pymysql

def get_connection():
    conn = pymysql.connect(host="127.0.0.1",user='root',password='1234',db='flaskDb',charset='utf8')
    if conn:
        print('디비접속 완료')
        print(conn)
    return conn
def get_member_list():
    conn=get_connection()
    cursor = conn.cursor()
    sql = ''' 
    select * from memberTBL order by USERNO desc;
    '''
    cursor.execute(sql)
    result2 = cursor.fetchall()
    temp_list =[]
    for row in result2:
        temp_dic = {}
        temp_dic['userNo']=row[0]
        temp_dic['userId']=row[1]
        temp_dic['userName']=row[2]
        temp_dic['pwd']=row[3]
        temp_list.append(temp_dic)
    conn.close()
    print("db연결 종료")
    return temp_list
def member_add(userId,userName,pwd):
    conn=get_connection()
    cursor = conn.cursor()
    sql = ''' 
    insert into membertbl (userId,userName,pwd) values(%s,%s,%s)
    '''
    cursor.execute(sql,(userId,userName,pwd))
    conn.commit()
    conn.close()
    print("db연결 종료")

def member(userId) :
    # 데이터베이스 접속
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문
    sql = '''SELECT * FROM memberTBL  where userId = %s  '''
    cursor.execute(sql, userId)

    # 결과를 가져온다. => 튜플 형태 
    result = cursor.fetchone()
    if result:
        # 데이터를 추출한다.
        temp_dic = {}
        temp_dic['userNo'] = result[0]
        temp_dic['userId'] = result[1]
        temp_dic['userName'] = result[2]
        temp_dic['pwd'] = result[3]

        conn.close()
        return temp_dic
    else:
        conn.close()
        return 0


def login_result(userId, pwd):
    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    sql = 'SELECT * FROM memberTBL WHERE userId=%s AND pwd=%s;'
    cursor.execute(sql,(userId,pwd))
    login_result = cursor.fetchone()
    if login_result:
        return True
        # return login_result
    else:
        return False

