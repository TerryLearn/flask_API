from app.libs.redprints import Redprint

api = Redprint('client')


@api.route('/register')
def create_client():
    #注册登录
    #参数校验
    pass