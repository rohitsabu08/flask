import re
from flask import Flask ,render_template,request
from flask.wrappers import Request
from werkzeug.wrappers import request

#WSGI
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def welcome():
    return render_template('index.html')

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to praxis {your_name}"

@app.route("/checking_req")
def get_req_parameters():
    name = request.args.get("studentname")
    roll_no = request.args.get("roll_no")
    return(f"Student name is {name} and roll number is {roll_no}")
    
if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0',port =3400)

