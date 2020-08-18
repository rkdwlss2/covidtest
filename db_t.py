# db.py
# 모듈 임포트 
# 미설치 pip install pymysql
import pymysql

# 데이터 베이스에 접속하는 함수
def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='sample1'
            , charset='utf8')
    if conn:
        print('디비 접속 완료')
        print(conn)
    return conn
# 연결 테스트 함수호출 
# get_connection()


# worldCity 테이블 전체 목록을 가져오는 함수
def get_country_list() :
    # 커서 생성
    conn = get_connection()
    cursor = conn.cursor()

    # sql문 쿼리문
    # no 기준으로 내림차순 정렬 
    sql = ''' SELECT * FROM worldCity ORDER BY no DESC  '''
    cursor.execute(sql)
    result = cursor.fetchall()

    # 딕셔너리 리스트 구조 
    temp_list = []
    for row in result:
        temp_dic = {}
        temp_dic['No'] = row[0]
        temp_dic['Code'] = row[1]
        temp_dic['Name'] = row[2]
        temp_dic['GNP'] = row[3]
        temp_dic['Population'] = row[4]
        temp_list.append(temp_dic)
    # 접속종료        
    conn.close()
    return temp_list  

# 전체 테이블 조회 테스트 
# print('---')
# print(get_country_list())


# no으로 나라별 레코드 반환함수 
def country(no) :
    # 커서 생성
    conn = get_connection()
    cursor = conn.cursor()

    # sql문 쿼리문
    sql = ''' SELECT * FROM worldCity WHERE No=%s  '''
    cursor.execute(sql, no)
    # 튜플구조로 반환 
    result = cursor.fetchone()
    # 딕셔너리 구조로 변환
    temp_dic = {}
    temp_dic['No'] = result[0]
    temp_dic['Code'] = result[1]
    temp_dic['Name'] = result[2]
    temp_dic['GNP'] = result[3]
    temp_dic['Population'] = result[4]
    # 접속종료        
    conn.close()
    return temp_dic

# print(country(10))


# 단어 검색후 반환 함수 
# 특정단어가 들어가는 레코드 검색 sql 구문 
# select * from worldcity where Name like "%단어%";
def search_country_list(name) :
    # 커서 생성
    conn = get_connection()
    cursor = conn.cursor()

    # sql문 쿼리문
    sql = ''' SELECT * FROM worldCity WHERE Name LIKE %s '''
    name = '%'+name+'%'
    cursor.execute(sql, name)
    result = cursor.fetchall()

    # 딕셔너리 리스트 구조 
    temp_list = []
    for row in result:
        temp_dic = {}
        temp_dic['No'] = row[0]
        temp_dic['Code'] = row[1]
        temp_dic['Name'] = row[2]
        temp_dic['GNP'] = row[3]
        temp_dic['Population'] = row[4]
        temp_list.append(temp_dic)
    # 접속종료        
    conn.close()
    return temp_list  

# print('-'*20)
# print(search_country_list('kor'))

# 레코드 추가함수 
def country_add(c_code, c_name, c_gnp, c_population):
    # 데이타베이스 접속후 작업변수 생성
    conn = get_connection()
    cursor = conn.cursor()

    # 레코드 추가와 관련된 sql
    # INSERT INTO 테이블명 (컬럼명1,...,컬럼명n) VALUES (값1, ... 값N);
    sql = '''
            INSERT INTO worldCity
                (code, name, gnp, population)
                values (%s, %s, %s, %s)
            '''
    cursor.execute(sql, (c_code, c_name, c_gnp, c_population))
    # DB 반영
    conn.commit()
    conn.close()

# 레코드 추가 테스트 
# country_add('FIN', 'Finland', 121914.00, 1376)
# country_add('FFF', 'FFFland', 121914.00, 1376)

# 레코드 삭제 
def country_delete(country_no):
    # 데이타베이스 접속
    conn = get_connection()
    cursor = conn.cursor()

    # 레코드 삭제와 관련된 sql 
    # DELETE from 테이블명 where 조건식;
    sql = '''
            DELETE FROM worldCity
                WHERE No = %s
            '''             
    cursor.execute(sql, (country_no))
    conn.commit()
    conn.close()

# 레코드 삭제 테스트 
# country_delete(5)


# 레코드 수정 함수 : gnp, population 컬럼만 수정 
# update 테이블명 set 컬럼명=값 where 조건식
def country_update(c_no, c_gnp, c_population):
    # 데이타베이스 접속함수 호출
    conn = get_connection()
    cursor = conn.cursor()

    # 레코드 수정 sql 구문 
    sql = '''
            update worldcity
                set 
                    GNP=%s, Population=%s
                where No=%s
            '''
    cursor.execute(sql, (c_gnp, c_population, c_no))
    conn.commit()
    conn.close()

# 레코드 수정 테스트 
country_update(32, 8, 8)