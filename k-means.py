from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
def k_means_demo():
    """

    :return:
    """
    data_new = [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6],
                [9, 11], [1, 3], [8, 9], [0, 3], [5, 4]]
    # 预估器流程
    estimator =  KMeans(n_clusters=3)
    estimator.fit(data_new)

    # 得出结果
    y_predict = estimator.predict(data_new)

    # 模型评估
    score = silhouette_score(data_new,y_predict)
    print("轮廓系数为:\n",score)
    return None
if __name__ == '__main__':
    k_means_demo()