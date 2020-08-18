from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index2.html')

@app.route('/about')
def about():    
    return render_template('about.html')

@app.route('/data')
def data():    
    return render_template('data.html')
@app.route('/bbs')
def bbs():    
    return render_template('bbs.html')

@app.route('/contact')
def contact():    
    return render_template('contact.html')

app.run(host='127.0.0.1', port=5000, debug=True)



