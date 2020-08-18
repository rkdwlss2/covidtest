from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index_calForm.html')

# 데이터 받기
@app.route('/cal',methods=['POST'])
def cal():    
    data1 =request.form['data1']
    data2 =request.form['data2']
    return render_template('cal_result.html',data1=int(data1),data2=int(data2))
    # return data1+'<br>'+data2

# 구구단
@app.route('/gugu',methods=['POST'])
def gugu():    
    data3 =request.form['data3']
    return render_template('gugu_result.html',data3=int(data3))
    # return data1+'<br>'+data2
@app.route('/nu',methods=['POST'])
def nu():    
    data4 =request.form['data4']
    return render_template('nu_result.html',data4=int(data4))
@app.route('/info',methods=['GET'])
def info():    
    userName =request.args['userName']
    userAge =int(request.args['userAge'])
    userYear=2020-userAge
    return render_template('info_result.html',userName=userName,userAge=userAge,userYear=userYear)
@app.route('/resultTotal/<int:no>')
def resultTotal(no):
    result = 0
    for i in range(no):
        result+=(i+1)
    return render_template('resultTotal.html',no=no,result=result)


# for i in myList:
#     print(i)
#     # return "hi"

# for key in myDict:
#     print(key,myDict[key])


app.run(host='127.0.0.3', port=5000, debug=True)



