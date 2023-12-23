from flask import Flask
from flask import render_template
from flask import request
from dbmanager import dbmanager
from appcfg import access
import service.user_account

app = Flask('tkynotebook')
db = dbmanager('tkynotebook.db')

##################################################
'''
接口界面
'''
###################################################
@app.route('/')
def welcome():
    return render_template('windows/welcome.html')

@app.route('/homepage', methods = ['GET'])
def homepage():
    input = request.args
    if 'access' not in input or input['access'] != access:
        return render_template('windows/welcome.html')
    return render_template('windows/homepage.html')



##################################################
'''
接口函数
'''
###################################################
@app.route('/login', methods = ['POST'])
def actionLogin():
    '''
    登录接口
    登录成功返回访问令牌
    '''
    must_params = ['account', 'password']
    input = request.get_json()

    for item in input.keys():
        if item not in must_params:
            return item + " was not found!"
    
    return service.user_account.check_login(db, input['account'], input['password'])