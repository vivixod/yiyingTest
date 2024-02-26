from flask import request
from flask.views import MethodView
from app.models import User


class LoginApi(MethodView):
    def post(self):
        form = request.json
        user_name = form.get('user_name')
        user_password = form.get('user_password')
        user = User.query.filter_by(user_name=user_name).first()
        if user is None:
            return {
                'status': 'error',
                'message': user_name + ' does not exist',
                'code': 1,
            }
        if user and user.verify_password(user_password):
            return {
                'status': 'success',
                'message': '登录成功',
            }
        else:
            return {
                'status': 'error',
                'message': '密码错误',
                'code': 2,
            }


login_view = LoginApi.as_view('login_api')
