from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
def linear_demo1():
    """
    正规方程的优化方法，预测房价
    :return:
    """
    # 获取数据集
    california = fetch_california_housing()

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(california.data, california.target, random_state=22)

    # 特征工程 -- 无量纲化（标准化）
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 预估器流程 -- 模型生成
    estimator = LinearRegression()
    estimator.fit(x_train,y_train)

    # 模型
    print("正规方程权重系数为：\n",estimator.coef_)
    print("正规方程偏置为：\n",estimator.intercept_)

    # 模型评估
    y_predict = estimator.predict(x_test)
    print("预测房价\n",y_predict)
    error  = mean_squared_error(y_test,y_predict)
    print("正规方程均方误差为\n",error)
    return None
def linear_demo2():
    """
    梯度下降优化房价预测
    :return:
    """
    # 获取数据集
    california = fetch_california_housing()

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(california.data, california.target, random_state=22)

    # 特征工程 -- 无量纲化（标准化）
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 预估器流程 -- 模型生成
    estimator = SGDRegressor(eta0=0.001,penalty="l1")
    estimator.fit(x_train, y_train)

    # 模型
    print("梯度下降权重系数为：\n", estimator.coef_)
    print("梯度下降偏置为：\n", estimator.intercept_)

    # 模型评估
    y_predict = estimator.predict(x_test)
    print("预测房价\n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("梯度下降均方误差为\n", error)
    return None

def linear_demo3():
    """
    岭回归对房价进行预测
    :return:
    """
    # 获取数据集
    california = fetch_california_housing()

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(california.data, california.target, random_state=22)

    # 特征工程 -- 无量纲化（标准化）
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 预估器流程 -- 模型生成
    estimator = Ridge(max_iter=10000)
    estimator.fit(x_train, y_train)

    # 模型
    print("岭回归权重系数为：\n", estimator.coef_)
    print("岭回归偏置为：\n", estimator.intercept_)

    # 模型评估
    y_predict = estimator.predict(x_test)
    print("预测房价\n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("岭回归均方误差为\n", error)
    return None
if __name__ == '__main__':
    # 正规方程
    linear_demo1()
    print("--------------------------------------------------------------")
    # 梯度下降
    linear_demo2()
    print("--------------------------------------------------------------")
    # 岭回归
    linear_demo3()