# flask 모듈 임포트
from flask import Flask, render_template, request, redirect, url_for,session
# db_t.py 임포트
import db4

# flask 객체 생성
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    # 테이블 레코드 저장 
    member_list = db4.get_member_list()
    return render_template('index_member.html', \
                            member_list=member_list, \
                            totalCount=len(member_list))
@app.route('/add')
def add():
    return render_template('add_member.html')

@app.route('/login')
def login():
    return render_template('loginForm.html')

@app.route('/add_pro',methods=['POST'])
def add_pro():
    userId = request.form['userId']
    userName = request.form['userName']
    pwd = request.form['pwd']
    if db4.member(userId):
        return render_template('fail.html')
    else:
        db4.member_add(userId,userName,pwd)
        return render_template('success.html')
@app.route('/login_pro', methods = ['POST'])
def login_pro():
    userId = request.form['userId']
    pwd = request.form['pwd']
    result=db4.login_result(userId,pwd)
    if result:
        session['userId'] = userId
    # return '<a href="/log_out">Log Out</a>'
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/log_out')
def log_out():
    session.pop('userId',None)
    print(session)
    return redirect('/')
app.run(host='127.0.0.1', port=5000, debug=True)  
# localhost:5000 접속후 확인 
# app.run(host='0.0.0.0', port=5000, debug=True)