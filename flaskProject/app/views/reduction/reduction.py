from sklearn.decomposition import PCA
import json
import os
import numpy as np
import pandas as pd

from flask import request
from flask.views import MethodView

from app.functions.KFRAD import KFRAD


class ReductionApi(MethodView):

    def __init__(self):
        self.col_count = None
        self.row_count = None

    def detection(self, df):
        # 将DataFrame转换为矩阵
        data_matrix = df.values
        self.row_count = df.shape[0]
        self.col_count = df.shape[1]
        # 创建PCA对象并拟合数据
        pca = PCA(n_components=2)  # 指定要保留的主成分数量
        X_reduced = pca.fit_transform(X)
        print(X_reduced)
        output = KFRAD(data_matrix, 0.02)

        # 在输入矩阵后面添加输出结果
        final_matrix = np.concatenate((data_matrix, output[:, np.newaxis]), axis=1)

        data_json = json.dumps(final_matrix.tolist())

        print(data_json)

        return data_json

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
        upload_folder = 'file'

        # 获取当前工作目录
        current_directory = os.getcwd()

        # 构建保存文件的完整路径
        save_path = os.path.join(current_directory, upload_folder, file.filename)

        # 保存文件
        file.save(save_path)

        # 从CSV文件中加载数据到DataFrame
        data_frame = pd.read_csv(save_path, encoding='utf-8')

        # 从CSV文件中加载数据的头部行
        header = pd.read_csv(save_path, encoding='utf-8', nrows=1)

        # 提取columns信息
        columns = header.columns.tolist()

        # 添加result元素
        columns.append("result")

        columns_json = {str(index): value for index, value in enumerate(columns)}

        data = self.detection(data_frame)
        # 返回保存成功的消息
        return {
            'status': 'success',
            'message': 'Sum calculated successfully',
            'data': data,
            'row_count': self.row_count,
            'col_count': self.col_count,
            'file': file.filename,
            'header': columns_json
        }


reduction_view = ReductionApi.as_view('reduction_api')

# # 示例数据集
# X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# # 创建PCA对象并拟合数据
# pca = PCA(n_components=2)  # 指定要保留的主成分数量
# X_reduced = pca.fit_transform(X)
#
# # 输出降维后的数据
# print("Original data shape:", X.shape)
# print("Reduced data shape:", X_reduced.shape)
# print("Reduced data:")
# print(X_reduced)
