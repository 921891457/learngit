
from flask import Flask,request,render_template,Blueprint,make_response
app = Flask(__name__)
cookie = Blueprint('cookie',__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
       return render_template('login.html')
    else:
       name = request.form.get('username')
       passowrd = request.form.get('password')
       res = make_response(render_template('hello.html',username=name,password=passowrd))
       res.set_cookie('name',name)
       return res
@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method=='GET':
        return render_template('hello.html',username='111',passowrd='111')