from flask import request
from flask.views import MethodView
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import base64
from io import BytesIO


class TestApi(MethodView):
    def post(self):
        # 数据准备
        y_label = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
        y_pre = [0.9, 0.8, 0.7, 0.6, 0.55, 0.54, 0.53, 0.52, 0.51, 0.505, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33,
                 0.3, 0.1]
        fpr, tpr, threshold = roc_curve(y_label, y_pre)
        roc_auc = auc(fpr, tpr)

        # 绘制 ROC 曲线
        plt.plot(fpr, tpr, 'k--', label='ROC (area = {0:.2f})'.format(roc_auc), lw=2)
        for i, value in enumerate(threshold):
            plt.text(fpr[i], tpr[i], f'{value:.2f}', fontsize=12, ha='right')

        plt.xlim([-0.05, 1.05])
        plt.ylim([-0.05, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve')
        plt.legend(loc="lower right")
        plt.savefig(r'D:\github\dachuang2024\src\assets\images\test.png')
        plt.show()

        # 将图像转换为 Base64 编码
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return {
            'status': 'success',
            'message': 'Sum calculated successfully',
            'image': image_base64
        }


test_view = TestApi.as_view('test_api')
