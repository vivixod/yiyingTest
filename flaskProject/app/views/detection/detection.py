import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from flask import request
from flask.views import MethodView

from app.functions.KFRAD import KFRAD


class DetectionApi(MethodView):

    def __init__(self):
        self.col_count = None
        self.row_count = None
        self.n = ''

    def detection(self, df):
        # 将DataFrame转换为矩阵
        data_matrix = df.values
        self.row_count = df.shape[0]
        self.col_count = df.shape[1]

        output = KFRAD(data_matrix, 0.02)
        # 找到目标的数值
        sorted_output = np.sort(output)
        # 找到最大值
        maximum_value = np.max(output)

        # 找到最小值
        minimum_value = np.min(output)

        # 绘制折线图
        plt.plot(output)

        if self.n != '':
            n = int(self.n)
            # 添加横线
            target = sorted_output[-n]
            plt.axhline(y=target, color='red')
            plt.annotate(round(target, 3), xy=(1, target), xytext=(-40, 10),
                         textcoords='offset points', arrowprops=dict(arrowstyle='->'))

        # 设置纵坐标范围
        plt.ylim(minimum_value, maximum_value)
        # 获取当前的坐标轴范围
        x_min, x_max = plt.xlim()
        # 设置横坐标刻度和标签，自动根据数据范围设置刻度
        plt.xticks(np.arange(int(x_min), int(x_max) + 1, step=1))
        plt.savefig(r'D:\github\yiyingTest\flaskProject\image\KFRAD_detection.png')
        # 显示图形
        # plt.show()

        final_matrix = np.concatenate((data_matrix, output[:, np.newaxis]), axis=1)
        if self.n != '':
            # 如果你想按降序排列，你可以这样获取索引：
            sorted_indices_descending = np.argsort(final_matrix[:, -1])[::-1]
            sorted_final_matrix_descending = final_matrix[sorted_indices_descending]
            sorted_final_matrix_top_n = sorted_final_matrix_descending[:n]
            detail_data_json = json.dumps(data_matrix.tolist())
            data_json = json.dumps(sorted_final_matrix_top_n.tolist())
            return data_json, detail_data_json
        else:
            detail_data_json = json.dumps(data_matrix.tolist())
            data_json = json.dumps(final_matrix.tolist())
            return data_json, detail_data_json

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

        self.n = request.form.get('n')

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

        data, detail_data = self.detection(data_frame)

        # 返回保存成功的消息
        return {
            'status': 'success',
            'message': 'Sum calculated successfully',
            'data': data,
            'row_count': self.row_count,
            'col_count': self.col_count,
            'file': file.filename,
            'header': columns_json,
            'detail_data': detail_data
        }


detection_view = DetectionApi.as_view('detection_api')
