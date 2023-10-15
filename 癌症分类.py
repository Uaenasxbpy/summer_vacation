import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
import joblib
def cancer_demo():
    """
    逻辑回归用来癌症预测
    :return:
    """
    # 获取数据 -- 读取数据加上names
    path = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
    colum_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
             'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
             'Normal Nucleoli', 'Mitoses', 'Class']
    data = pd.read_csv(path,names=colum_name)
    # print(data)

    # 数据处理 -- 处理缺失值
    # 替换成np.nan
    data = data.replace(to_replace="?",value=np.nan)
    # 删除缺失样本 -- 删除行
    data.dropna(inplace=True)
    # print(data)

    # 数据集划分
    # 筛选特征值和目标值
    x = data.iloc[:,1:-1]
    y = data["Class"]
    # print(x)
    # print(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # 特征工程 -- 无量纲化（标准化）
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 逻辑回归预估器
    estimator = LogisticRegression()
    estimator.fit(x_train,y_train)
    print("权重系数：\n",estimator.coef_)
    print("权重系数：\n",estimator.intercept_)

    # 模型保存
    joblib.dump(estimator,"my_ridge.pkl")

    # 加载模型
    estimator = joblib.load("my_ridge.pkl")

    # 模型评估
    # 方法1
    y_predict = estimator.predict(x_test)
    print("预测结果：\n",y_predict)
    print("预测值与真实值的比较：\n",y_test == y_predict)
    score = estimator.score(x_test,y_test)
    print("准确率为：\n",score)
    # 方法2 -- 查看精确率和召回率，F1-score
    report = classification_report(y_test,y_predict,labels=[2,4],target_names=["良性","恶性"])
    print(report)

    # 方法3 -- AUC和ROC
    y_true = np.where(y_test > 3,1,0)
    aoc = roc_auc_score(y_true,y_predict)
    print("AUC指标：\n",aoc)

    return None
if __name__ == "__main__":
    cancer_demo()