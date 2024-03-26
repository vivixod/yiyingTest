from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def knn_predict(train_X, train_y, sample_X, k=2):
    # 创建并训练KNN分类器
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_X, train_y)

    # 预测单个样本
    sample_y = knn.predict([sample_X])

    return sample_y


# 示例训练集
train_X = [[1, 2], [3, 4], [5, 6], [7, 8]]
train_y = [0, 0, 1, 1]

# 示例测试样本
sample_X = [4, 5]

# 使用修改后的代码进行预测
sample_y_pred = knn_predict(train_X, train_y, sample_X)

print("Predicted class:", sample_y_pred)
