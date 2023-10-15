import os
import time
import multiprocessing
# 跳舞
def dance():
    """
    :return:
    """
    for i in range(3):
        print("跳舞...")
        time.sleep(0.5)
    return None

# 唱歌
def sing():
    """
    :return:
    """
    for i in range(3):
        print("唱歌...")
        time.sleep(0.5)
    return None

# 有参数的函数
# args:以元组的方法传参,必须保证按顺序。
# kwargs:以字典的方法传参，保证键值对匹配。
def basketball(name,num):
    """
    :return:
    """
    print("打篮球的进程编号：",os.getpid())
    print("打篮球的进程的父进程的编号：",os.getppid())
    for i in range(num):
        print(f"{name}在星期{i + 1}打篮球！")
    return None
def pingpong(name,num):
    """
    :return:
    """
    print("打乒乓球的进程编号：", os.getpid())
    print("打乒乓球的进程的父进程的编号：", os.getppid())
    for i in range(num):
        print(f"{name}在星期{i + 1}打乒乓球！")
    return None

if __name__ == '__main__':
    print("主进程编号为：",os.getpid())
    # 单进程任务
    # sing()
    # dancce()

    # 多进程任务
    # 1.导入进程包 -- multiprocessing
    # 2.使用进程类创建进程对象
    # target的参数为执行的函数名
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)
    # 3.使用进程对象启动进程任务
    # 设置守护主进程，即为主进程结束后就把子进程也结束了
    dance_process.daemon = True
    sing_process.daemon = True
    dance_process.start()
    sing_process.start()

    # 有参数的进程
    basketball_process = multiprocessing.Process(target=basketball,args=("张三",3,))
    pingpong_process = multiprocessing.Process(target=pingpong,kwargs={"name":"李四","num":4})
    # basketball_process.start()
    # pingpong_process.start()

    # 获取进程的编号
    # os.getpid(),os.getppid()
    time.sleep(1)
    print("主进程结束了！")
