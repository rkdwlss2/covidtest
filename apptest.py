# flask 모듈 임포트
# session 모듈 임포트
from flask import Flask, render_template, request, redirect, url_for,session


# flask 객체 생성
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    # 테이블 레코드 저장 
    return render_template('loginForm.html')

@app.route('/login_pro', methods = ['POST'])
def login_pro():
    userId = request.form['userId']
    pwd = request.form['pwd']
    session['userId'] = userId
    print(session) # <SecureCookieSession {'userId': 'coderecipe'}>
    # return '<a href="/log_out">Log Out</a>'
    return redirect('/')

@app.route('/log_out')
def log_out():
    session.pop('userId',None)
    print(session)
    return redirect('/')

app.run(host='127.0.0.1', port=5000, debug=True)  
# localhost:5000 접속후 확인 
# app.run(host='0.0.0.0', port=5000, debug=True)