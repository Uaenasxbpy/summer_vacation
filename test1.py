from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import jieba
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
import pandas as pd
from scipy.stats import pearsonr
from sklearn.decomposition import PCA

def datasets_demo():
    """
    sklearn数据集的使用
    :return:
    """
    # 获取数据集
    iris = load_iris()
    # print("鸢尾花数据集的返回值为：\n", iris)
    print("查看数据集的描述：\n",iris["DESCR"])
    print("查看特征值的名字\n",iris.feature_names)
    print("查看目标值的名字\n",iris.target_names)

    # 数据集划分
    # 训练集的特征值 测试集的特征值 训练集的目标值 测试集的目标值
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)  # test_size默认0.25
    print("训练集的特征值：\n",x_train,x_train.shape)
    return None

def dict_demo():
    """
    字典特征提取
    :return:
    """
    x = [{'color': 'red', 'size': 'S'},
         {'color': 'blue', 'size': 'M'},
         {'color': 'green', 'size': 'L'}]
    data = [{'city': '北京','temperature': '100'},
            {'city': '上海','temperature': '60'},
            {'city': '深圳','temperature': '30'}]
    # 实例化一个转换器类
    transfer = DictVectorizer(sparse=False)

    #调用fit_transform()方法
    data_new = transfer.fit_transform(data)

    # data_new_x = transfer.fit_transform(x)
    print("data_new:\n",data_new)

    # 使用其get_feature_names_out()方法来获取特征的名称列表
    name = transfer.get_feature_names_out()
    print(f"特征名字：{name}")
    # print("data_new_x:\n",data_new_x)

def text_demo():
    """
    文本特征提取
    :return:
    """
    # 文本数据
    text_data = [
        "I love coding and machine learning",
        "Coding is fun",
        "Machine learning is interesting",
        "I want to become a data scientist",
        "Python is a popular programming language"
    ]
    text_data_zh = [
        "我喜欢编程和机器学习",
        "编程很有趣",
        "机器学习很有意思",
        "我想成为一名数据科学家",
        "Python是一门流行的编程语言"
    ]
    # jieba分词
    text_data_zh_segmented = [" ".join(jieba.cut(text)) for text in text_data_zh]

    # 查看Scikit-learn的英文停用词表集合
    # print(ENGLISH_STOP_WORDS)

    # 1.创建一个CountVectorizer对象
    vectorizer = CountVectorizer(stop_words=list(ENGLISH_STOP_WORDS))
    vectorizer_zh = CountVectorizer()

    # 调用fit_transform方法
    data_new = vectorizer.fit_transform(text_data)
    data_new_zh = vectorizer_zh.fit_transform(text_data_zh_segmented)

    # toarray()方法把稀疏矩阵转化成矩阵
    print(f'data_new:{data_new.toarray()}')
    print(f'文本的特征名字：{vectorizer.get_feature_names_out()}')

    print(f'data_new_zh:{data_new_zh.toarray()}')
    print(f'文本的特征名字：{vectorizer_zh.get_feature_names_out()}')

def tfidf_demo():
    """
    用TFIDF方法进行文本特征抽取
    :return:
    """
    # 文本数据
    text_data = [
        "I love coding and machine learning",
        "Coding is fun",
        "Machine learning is interesting",
        "I want to become a data scientist",
        "Python is a popular programming language"
    ]
    # 1.创建一个CountVectorizer对象
    vectorizer = TfidfVectorizer(stop_words=list(ENGLISH_STOP_WORDS))

    # 调用fit_transform方法
    data_new = vectorizer.fit_transform(text_data)

    # toarray()方法把稀疏矩阵转化成矩阵
    print(f'data_new:{data_new.toarray()}')
    print(f'文本的特征名字：{vectorizer.get_feature_names_out()}')

def cut_words(text):
    """
    进行中文分词，并进行停用词过滤
    :param text: 待分词的中文文本
    :return: 分词后的结果，以空格分隔的字符串形式返回
    """
    # 加载停用词表
    stopwords = set()
    with open("数据文件/stopwords.txt", "r", encoding="utf-8") as f:
        for line in f:
            stopwords.add(line.strip())

    # 中文分词并过滤停用词
    words = [word for word in jieba.cut(text) if word not in stopwords]
    result = " ".join(words)
    # 返回结果
    return result

def minmax_demo():
    """
    归一化
    :return:
    """
    # 获取数据
    data = pd.read_csv("数据文件/dating.txt")
    data = data.iloc[:,:3]
    # print(data)
    # 实例化一个类
    minmax = MinMaxScaler(feature_range=(0,1))
    # 调用fit_transform方法
    data_new = minmax.fit_transform(data)
    print(f'归一化后的数据为:{data_new}')

def stand_demo():
    """
    标准化
    :return:
    """
    # 获取数据
    data = pd.read_csv("数据文件/dating.txt")
    data = data.iloc[:,:3]
    # 创建实例
    stand = StandardScaler()
    # 调用方法
    data_new = stand.fit_transform(data)
    print(f"标准化后的数据为\n：{data_new}")

def variance_demo():
    """
    低方差数据过滤
    相关系数计算
    :return:
    """
    # 获取数据
    data = pd.read_csv("数据文件/test.csv")
    data = data.iloc[:,:4]
    print(f"数据为：{data,data.shape}")
    # 实例化
    variance = VarianceThreshold()
    # 调用方法
    data_new = variance.fit_transform(data)
    print(data_new,data_new.shape)
    # 计算相关系数
    R = pearsonr(data["weight"],data["height"])
    print(f"体重和身高的相关系数为\n{R[0]}")
    print(f"检验中的显著性水平:\n{R[1]}")

def pca_demo():
    """
    PCA降维
    :return:
    """
    data = [
        [2,8,4,5],
        [6,3,0,8],
        [5,4,9,1]
    ]
    # 实力化一个类
    pca = PCA(n_components=2)
    # 调用方法
    data_new = pca.fit_transform(data)
    # 获取主成分和方差
    components = pca.components_
    explained_variance = pca.explained_variance_
    print(f"主成分和方差为{components},{explained_variance}")
    print(data_new)
if __name__ == "__main__":
    # datasets_demo()
    # dict_demo()
    # text_demo()
    # tfidf_demo()
    # minmax_demo()
    # stand_demo()
    # variance_demo()
    # pca降维
    pca_demo()