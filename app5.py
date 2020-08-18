from flask import Flask,render_template,request,redirect,url_for
import db3
app = Flask(__name__)

@app.route('/')
def index():    
    #테이블 레코드 저장
    emp_list=db3.get_emp_list()
    return render_template('index_empList.html',emp_list=emp_list,totalCount=len(emp_list))


@app.route('/emp_view/<no>')
def emp_view(no):
    emp_data=db3.get_empone_list(no)
    return render_template('detail_view.html',emp_data=emp_data)

@app.route('/emp_add')
def emp_add():
    return render_template('emp_add.html')

@app.route('/emp_add_pro',methods=['post'])
def emp_add_pro():
    c_first_name=request.form['c_first_name']
    c_last_name=request.form['c_last_name']
    c_gender=request.form['c_gender']
    c_birth=request.form['c_birth']
    db3.emp_add(c_first_name,c_last_name,c_gender,c_birth)
    return redirect(url_for('emp_add'))

@app.route('/emp_delete/<no>')
def emp_delete(no):
    db3.emp_delete(no)
    return redirect('/')

@app.route('/emp_update/<emp_no>')
def emp_update(emp_no) :
    emp_dict = db3.get_empone_list(emp_no)
    return render_template('emp_update.html', emp_dict=emp_dict)
    # return render_template('country_update.html')
@app.route('/emp_update_pro', methods=['post'])
def emp_update_pro():
    c_no = request.form['c_no']
    c_first_name = request.form['c_first_name']
    c_last_name = request.form['c_last_name']
    c_gender = request.form['c_gender']
    c_birth = request.form['c_birth']  
    db3.emp_update(c_no, c_first_name, c_last_name,c_gender,c_birth)
    return redirect(url_for('emp_view',no=int(c_no)))
app.run(host='127.0.0.1', port=5000, debug=True)



