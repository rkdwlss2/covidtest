from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():    
    #변수 정의
    userName = '홍길동'
    userAge = 27
    myList=['사과','포도','망고']
    myTuple=(100,200,300,400)
    myDict={'a':'apart','b':'banana','c':'cat'}
    return render_template('index_var.html',userName=userName,\
        userAge=userAge,myList=myList,myTuple=myTuple,\
            myDict=myDict)











# @app.route('/test1')
# def test1():
#     return '<h1>test1</h1><hr><a href="/">start Page</a>'

# @app.route('/test1/sub1')
# @app.route('/test1/sub2')
# def test1_sub():
#     return '<h1>test1 sub1 또는 test1 sub2</h1><hr><a href="/">start Page</a>'

# #쿼리 스트링 방식으로 데이타 전달후 출력
# @app.route('/test2/<data1>')
# def test2(data1):
#     return 'data1 = %s' % data1

# @app.route('/test2/<data1>/<data2>')
# def test2_data1_data2(data1,data2):
#     return 'data1 = %s,data2=%s <hr><a href="/">start Page</a>' % (data1,data2)

# #쿼리 스트링방식으로 데이터 전달 및 출력
# #/라우터주소/<데이터값>
# #라우터주소/<자료형:데이터값>
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % username

# @app.route('/user/<username>/<int:age>')
# def show_user_profile_age(username, age):
#     return 'Username %s, 나이 %d' % (username, age)
# #http://127.0.0.1/user/홍길동/23/암행어사
# @app.route('/user/<username>/<int:age>/<job>')
# def show_user_profile_age_job(username, age,job):
#     return 'Username %s, 나이 %d, 직업 %s' % (username, age,job)

app.run(host='127.0.0.2', port=5000, debug=True)


