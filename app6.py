# flask 모듈 임포트
from flask import Flask, render_template, request, redirect, url_for
# db_t.py 임포트
import db_t

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    # 테이블 레코드 저장 
    country_list = db_t.get_country_list()
    return render_template('index_countryList.html', \
                            country_list=country_list, \
                            totalCount=len(country_list))


# 하이퍼링크로 전달받은 no 값을 연결하는 라우터 등록 
@app.route('/country/<no>')
def country(no):
    temp_dic = db_t.country(no)
    # return str(temp_dic)
    return render_template('country.html', temp_dic=temp_dic )


# 검색 결과 연결 라우터 
@app.route('/search_list', methods=['GET'])
def search_list():
    # 검색필드에서 값 전달 
    country_name = request.args['country_name']
    # country_name = request.args.get('country_name')
    # 데이타베이스에서 검색된 레코드 반환 
    country_list = db_t.search_country_list(country_name)
    # return str(country_list)
    return render_template('search_country_list.html', \
                            country_list=country_list, \
                            totalCount=len(country_list), \
                                country_name=country_name)


# 회원 추가 : country_add
@app.route('/country_add')
def country_add():
    return render_template('country_add.html')

# 폼에서 받은 데이타를 db_t에 추가. 추가후에 첫번째 페이지로 이동 
@app.route('/country_add_pro', methods=['POST'])
def country_add_pro():
    # 입력필드값 전달 
    c_code = request.form['c_code']
    c_name = request.form['c_name']
    c_gnp = request.form['c_gnp']
    c_population = request.form['c_population']
    # db_t에 추가 
    db_t.country_add(c_code, c_name, c_gnp, c_population)
    # return '레코드 추가 완료'+'<br><a href="/">첫번째 페이지</a>'
    # redirect('주소') : 주소로 이동 
    # return redirect('/')
    # url_for('주소에해당하는뷰함수명'): 뷰함수에 해당하는 주소 반환 
    return redirect(url_for('index'))

# 레코드 삭제 확인 페이지로 이동
@app.route('/country_delete/<no>')
def country_delete(no):
    temp_dic = db_t.country(no)
    return render_template('country_delete.html', temp_dic=temp_dic )

# 레코드 삭제 후  첫번째 페이지로 이동
@app.route('/country_delete_pro/<country_no>')
def country_delete_pro(country_no):
    db_t.country_delete(country_no)
    return redirect('/')


# 레코드 수정 페이지 
# 쿼리스트링 방식
@app.route('/country_update/<country_no>')
def country_update(country_no) :
    temp_dic = db_t.country(country_no)
    return render_template('country_update.html', temp_dic=temp_dic)


# 레코드 수정 데이타 값을 db_t에 반영 
@app.route('/country_update_pro', methods=['post'])
def country_update_pro():
    c_no = request.form['c_no']
    c_gnp = request.form['c_gnp']
    c_population = request.form['c_population']
    db_t.country_update(c_no, c_gnp, c_population)
    # db_t 반영후 시작 페이지로 이동
    # return redirect('/')
    # url_for('뷰함수명', 변수=변수)
    # return redirect(url_for('index'))
    # 레코드 상세 페이지로 이동 
    return redirect(url_for('country', no=int(c_no)) )



# 앱 실행 
app.run(host='127.0.0.1', port=5000, debug=True)  
# localhost:5000 접속후 확인 
# app.run(host='0.0.0.0', port=5000, debug=True)