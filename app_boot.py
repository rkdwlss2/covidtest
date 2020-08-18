from flask import Flask,render_template,request,redirect,url_for
import db3
app = Flask(__name__)

@app.route('/')
def index():    
    #테이블 레코드 저장
    return render_template('index_boot.html')

app.run(host='127.0.0.1', port=5000, debug=True)



