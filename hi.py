from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

#print(app)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
# 함수 등록
def index():
    # return '<h1>Hello World</h1><hr><h2>Flask App start</h2>'
    
    # return render_template('index.html')
    return render_template('index.html')
# 
@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/third')
def third():
    return render_template('third.html')
@app.route('/result',methods=['POST'])
def result():
    print('요청방식 : ',request.method)
    # if request.method=='POST':
    #     return render_template('post.html')
    # if request.method=='GET':
    #     return render_template('get.html')
    # request.args['변수']
    # request.args.get('변수')
    # request.values.get('변수')
    # data1 = request.args['data1']
    # data2 = request.args.get('data2')
    # data3 = request.values.get('data2')

    # request.form['변수']
    # request.form.get('변수')
    # request.form.values.get('변수')
    data1 = request.form['data1']
    data2 = request.form.get('data2')
    data3 = request.values.get('data2')
    
    # return  'data1 : ' + data1 +  ' , data2 : '\
    #      + data2 +  ' , data3 : ' + data3 \
    #          +'<hr><a href="/">첫번째 페이지</a>'
    return f'data1 : {data1}, data2 : {data2}, data3 : {data3} <hr><a href="/">첫번째 페이지</a>'

    # 앱 실행
# 웹주소와 포트 지정
# 127.0.0.1:5000
app.run(host='0.0.0.0', port=5000, debug=True)
# localhost:5000
# app.run(host='0.0.0.0', port=5000, debug=True)
