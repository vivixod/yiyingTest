import os
from flask import request
from flask.views import MethodView


class FileApi(MethodView):
    def post(self):
        # 检查是否有文件上传
        if 'file' not in request.files:
            return {
                'status': 'error',
                'message': 'No file provided',
                'code': 1
            }

        # 获取上传的文件
        file = request.files['file']

        # 检查文件是否存在
        if file.filename == '':
            return {
                'status': 'error',
                'message': 'No file selected',
                'code': 2
            }

        # 指定相对路径保存文件，相对于当前工作目录
        upload_folder = os.path.join('..', 'file')

        # 获取当前工作目录
        current_directory = os.getcwd()

        # 构建保存文件的完整路径
        save_path = os.path.join(current_directory, upload_folder, file.filename)

        # 保存文件
        file.save(save_path)

        # 返回保存成功的消息
        return {
            'status': 'success',
            'message': 'File saved successfully',
            'code': 0
        }


file_view = FileApi.as_view('file_api')
