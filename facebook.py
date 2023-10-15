import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
def facebook_demo():
    """
    预测facebook签到位置.
    文件说明 train.csv, test.csvrow
    id：签入事件的id
    x y：坐标
    accuracy: 准确度,定位精度
    time: 时间戳
    place_id: 签到的位置，这也是你需要预测的内容
    :return:
    """
    # 获取数据
    data = pd.read_csv("数据文件/train.csv")
    # print(data)

    # 数据处理
    # 1） 缩小数据范围
    data = data.query("x < 9 & x > 3 & y < 9 & y > 3 ")
    # 2） 处理时间特征
    time_value = pd.to_datetime(data["time"],unit="h")
    date = pd.DatetimeIndex(time_value)
    # print(date.year)
    data["day"] = date.day
    data["weekday"] = date.weekday
    data["hour"] = date.hour


    # print(data.head())
    # 3) 过滤地点
    place_count = data.groupby("place_id").count()["row_id"]
    # print(place_count)
    place_count = place_count[place_count > 1] # 过滤小于2的地点
    # print(place_count)
    data_final = data[data["place_id"].isin(place_count[place_count > 1].index.values)]
    # print(data_final)
    # 筛选特征值
    x = data_final[["x","y","accuracy","day","weekday","hour"]]
    y = data_final[["place_id"]]

    # 数据集划分
    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=5)

    # 特征工程 -- 标准化
    transfer  = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # KNN算法预估流程
    estimator = KNeighborsClassifier()

    # 网格搜索与交叉验证
    param_dict = {"n_neighbors":[3,5,7,9]}
    estimator = GridSearchCV(estimator,param_grid=param_dict,cv=3)
    estimator.fit(x_train,y_train)

    # 模型选择与调优
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("y_test；\n",y_test)
    print("直接比对真实值和预测值：\n", y_test == y_predict)  # 将测试数据的标准值与预测值比对

    # 模型评估
    score = estimator.score(x_test, y_test)
    print("准确率：\n", score)
    print("最佳参数：\n", estimator.best_params_)
    print("最佳结果：\n", estimator.best_score_)
    print("最佳估计器：\n", estimator.best_estimator_)
    print("交叉验证结果：\n", estimator.cv_results_)

def decision_iris():
    """
    用决策树对鸢尾花分类
    :return:
    """
    # 或取数据集
    iris = load_iris()

    # 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=6)

    # 用决策树生成模型
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train,y_train)

    # 1)可视化决策树

    dot_data = export_graphviz(estimator, out_file="可视化.dot",
                               feature_names=iris.feature_names,
                               class_names=iris.target_names,
                               filled=True, rounded=True,
                               special_characters=True)
    # graph = pydotplus.graph_from_dot_data(dot_data)
    # graph.write_pdf("决策树可视化.pdf")
    # Image(graph.create_png())

    # 2)绘制决策树
    plt.figure(figsize=(10, 8))
    plot_tree(estimator, feature_names=iris.feature_names, class_names=list(iris.target_names), filled=True)
    plt.show()

    # 模型评估
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值：\n", y_test == y_predict)  # 将测试数据的标准值与预测值比对
    score = estimator.score(x_test,y_test)
    print(f"准确率为：{score}")
    return None

if __name__ == '__main__':
    # facebook_demo()
    decision_iris()