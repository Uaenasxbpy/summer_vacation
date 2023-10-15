from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
def knn_iris():
    """
    用KNN算法对鸢尾花分类
    :return:
    """
    # 获取数据
    iris = load_iris()
    # 数据划分
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=6)
    # 特征工程  --  标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # KNN预估流程
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)    # 获取分类模型
    # 模型评估
    y_predict = estimator.predict(x_test)    # 将测试数据的特征值传入获取预测值
    print("y_predict:\n",y_predict)
    print("直接比对真实值和预测值：\n",y_test == y_predict)    # 将测试数据的标准值与预测值比对
    score = estimator.score(x_test,y_test)
    print("准确率：\n",score)

def knn_iris_gscv():
    """
    用KNN算法对鸢尾花分类,
    添加网格搜索和交叉验证
    :return:
    """
    # 获取数据
    iris = load_iris()
    # 数据划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 特征工程  --  标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # KNN预估流程
    estimator = KNeighborsClassifier()

    # 添加网格搜索和交叉验证
    # 参数准备
    param_dict = {"n_neighbors":[1,3,5,7,9,11]}
    estimator = GridSearchCV(estimator,param_grid=param_dict,cv=10)

    estimator.fit(x_train, y_train)  # 获取分类模型
    # 模型评估
    y_predict = estimator.predict(x_test)  # 将测试数据的特征值传入获取预测值
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值：\n", y_test == y_predict)  # 将测试数据的标准值与预测值比对
    score = estimator.score(x_test, y_test)
    print("准确率：\n", score)

    print("最佳参数：\n",estimator.best_params_)
    print("最佳结果：\n",estimator.best_score_)
    print("最佳估计器：\n",estimator.best_estimator_)
    print("交叉验证结果：\n",estimator.cv_results_)

if __name__ == '__main__':
    # knn_iris()
    # 网格搜索和交叉验证
    knn_iris_gscv()