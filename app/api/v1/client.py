from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprints import Redprint
from app.validators.forms import ClientForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    #注册登录
    #参数校验
    # WTForms 验证表单
    #表单 JSON
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        }
    pass


def __register_user_by_email():
    pass