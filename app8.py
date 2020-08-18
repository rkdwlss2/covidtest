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
    return render_template('index_small.html')

@app.route('/login')
def login():
    return render_template('login2.html')



@app.route('/update')
def update():
    return render_template('update2.html')
app.run(host='127.0.0.1', port=5000, debug=True)  
# localhost:5000 접속후 확인 
# app.run(host='0.0.0.0', port=5000, debug=True)