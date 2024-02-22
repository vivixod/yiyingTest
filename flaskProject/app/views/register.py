from flask import request
from flask.views import MethodView
from app.extension import db
from app.models import User


class RegisterApi(MethodView):

    def post(self):
        form = request.json
        user = User()
        user.user_name = form.get('user_name')
        user.password = form.get('user_password')
        db.session.add(user)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据添加成功'
        }


register_view = RegisterApi.as_view('register_api')
