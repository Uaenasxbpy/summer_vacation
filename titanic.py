import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
def titanic_demo():
    """
    用决策树判断泰坦尼克号幸存者的概率
    :return:
    """
    # 1）获取数据
    titanic = pd.read_csv("数据文件/titanic/train.csv")
    # print(titanic)

    # 2)筛选特征值和目标值
    x = titanic[["Pclass","Age","Sex"]]
    y = titanic["Survived"]
    # print(x)
    # print(y)

    # 3) 数据处理 -- 缺失值处理,fillna函数用于填充缺失值，
    # 代码中使用了x["Age"].fillna(x["Age"].mean(), inplace=True)来将Age列中的缺失值用平均值进行填充
    x["Age"].fillna(x["Age"].mean(), inplace=True)
    # 转换成字典
    x = x.to_dict(orient="records")
    # print(x)

    # 4) 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state= 22)

    # 字典特征抽取
    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 5) 用决策树生成模型
    estimator = DecisionTreeClassifier(criterion="entropy",max_depth=7)
    estimator.fit(x_train, y_train)

    # 7) 绘制决策树
    # plt.figure(figsize=(16, 9))
    # plot_tree(estimator, feature_names=transfer.get_feature_names_out().tolist(), filled=True)
    # plt.show()

    # 8) 模型评估
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值：\n", y_test == y_predict)  # 将测试数据的标准值与预测值比对
    score = estimator.score(x_test, y_test)
    print(f"准确率为：{score}")

    return None
def demo1():
    """
    添加了网格搜索和交叉验证
    :return:
    """
    # 1）获取数据
    titanic = pd.read_csv("数据文件/titanic/train.csv")

    # 2)筛选特征值和目标值
    x = titanic[["Pclass", "Age", "Sex"]]
    y = titanic["Survived"]

    # 3) 数据处理 -- 缺失值处理,fillna函数用于填充缺失值，
    # 代码中使用了x["Age"].fillna(x["Age"].mean(), inplace=True)来将Age列中的缺失值用平均值进行填充
    x["Age"].fillna(x["Age"].mean(), inplace=True)
    # 转换成字典
    x = x.to_dict(orient="records")

    # 4) 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 字典特征抽取
    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 5) 用决策树生成模型
    estimator = DecisionTreeClassifier()

    # 设置参数候选值
    param_grid = {
        'criterion': ['gini', 'entropy'],
        'max_depth': [3, 5, 7, 9, 11]
    }

    # 网格搜索
    grid_search = GridSearchCV(estimator, param_grid=param_grid, cv=5)
    grid_search.fit(x_train, y_train)

    # 输出最佳参数和最佳得分
    print("Best parameters found: ", grid_search.best_params_)
    print("Best score: ", grid_search.best_score_)

    # 获取最佳模型
    estimator = grid_search.best_estimator_

    # 7) 绘制决策树
    # plt.figure(figsize=(16, 9))
    # plot_tree(estimator, feature_names=transfer.get_feature_names_out().tolist(), filled=True)
    # plt.show()

    # 8) 模型评估
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值：\n", y_test == y_predict)  # 将测试数据的标准值与预测值比对
    score = estimator.score(x_test, y_test)
    print(f"准确率为：{score}")

    return None
def demo2():
    """
    用随机森林来预测
    :return:
    """
    # 1）获取数据
    titanic = pd.read_csv("数据文件/titanic/train.csv")
    # print(titanic)

    # 2)筛选特征值和目标值
    x = titanic[["Pclass", "Age", "Sex"]]
    y = titanic["Survived"]
    # print(x)
    # print(y)

    # 3) 数据处理 -- 缺失值处理,fillna函数用于填充缺失值，
    # 代码中使用了x["Age"].fillna(x["Age"].mean(), inplace=True)来将Age列中的缺失值用平均值进行填充
    x["Age"].fillna(x["Age"].mean(), inplace=True)
    # 转换成字典
    x = x.to_dict(orient="records")
    # print(x)

    # 4) 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 字典特征抽取
    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    estimator = RandomForestClassifier()
    # 加入网格搜索和交叉验证
    param_dict = {
        "n_estimators":[120,200,300,500,800,1200],
        "max_depth":[5,8,12,11]
    }
    estimator = GridSearchCV(estimator,param_grid=param_dict,cv=3)
    estimator.fit(x_train,y_train)
    # 模型评估
    y_predict = estimator.predict(x_test)  # 将测试数据的特征值传入获取预测值
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值：\n", y_test == y_predict)  # 将测试数据的标准值与预测值比对
    score = estimator.score(x_test, y_test)
    print("准确率：\n", score)

    print("最佳参数：\n", estimator.best_params_)
    print("最佳结果：\n", estimator.best_score_)
    print("最佳估计器：\n", estimator.best_estimator_)
    print("交叉验证结果：\n", estimator.cv_results_)

    return None
if __name__ == '__main__':
    # titanic_demo()
    # demo1()
    demo2()