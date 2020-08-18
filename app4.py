from flask import Flask,render_template,request,redirect,url_for
import db2
app = Flask(__name__)

@app.route('/')
def index():    
    #테이블 레코드 저장
    country_list=db2.get_country_list()
    return render_template('index_countryList.html',country_list=country_list,total=len(country_list))

@app.route('/country/<no>')
def country(no):    
    #테이블 레코드 저장
    country_dict=db2.country(no)
    # return render_template('index_countryList.html')
    # return str(country_dict)
    return render_template('country.html',country_dict=country_dict)
@app.route('/search_list',methods=['GET'])
def search_list():    
    #테이블 레코드 저장
    country_name=request.args['country_Name']
    # return render_template('index_countryList.html')
    # return str(country_dict)
    country_list=db2.search_country_list(country_name)
    return render_template('search_country_list.html',country_list=country_list,total=len(country_list),country_name=country_name)
    # return str(country_list)

@app.route('/country_add')
def country_add():    
    return render_template('country_add.html')

@app.route('/country_add_pro',methods=['post'])
def country_add_pro():
    c_code=request.form['c_code']
    c_name=request.form['c_name']
    c_gnp=request.form['c_gnp']
    c_population=request.form['c_population']
    db2.country_add(c_code,c_name,c_gnp,c_population)
    # return '레코드 추가 완료'+'<br><a href="/">첫번째 페이지</a>'
    # return redirect('/')
    return redirect(url_for('country_add'))

@app.route('/country_delete/<country_no>')
def country_delete(country_no):
    country_dict=db2.country(country_no)
    return render_template('country_delete.html',country_dict=country_dict)

@app.route('/country_delete_pro/<country_no>')
def country_delete_pro(country_no):
    db2.country_delete(country_no)
    return redirect('/')

@app.route('/country_update/<country_no>')
def country_update(country_no) :
    country_dict = db2.country(country_no)
    return render_template('country_update.html', country_dict=country_dict)
    # return render_template('country_update.html')
@app.route('/country_update_pro', methods=['post'])
def country_update_pro():
    c_no = request.form['c_no']
    c_gnp = request.form['c_gnp']
    c_population = request.form['c_population']
    db2.country_update(c_no, c_gnp, c_population)
    return redirect(url_for('country',no=int(c_no)))






app.run(host='127.0.0.1', port=5000, debug=True)



