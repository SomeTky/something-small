from dbmanager import dbmanager
from appcfg import access

def check_login(db: dbmanager, account: str, password: str):
    '''
    检查登录，如果登录成功返回通行证否则返回错误信息
    '''
    user_info = dict()
    info = db.get_one_cond('user_account', ('account', account))
    print(info)
    if not info:
        return "账号不存在"
    
    user_info['account'] = info[1]
    user_info['password'] = info[2]

    if user_info['account'] != account:
        raise Exception('Unknow error')
    
    if user_info['password'] == password:
        return access
    else:
        return "密码错误"