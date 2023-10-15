# 多线程任务
# 导入线程模块
import threading
import time
# 创建线程对象
# 启动线程
def sing(name,num):
    """
    :param name:
    :param num:
    :return:
    """
    for i in range(num):
        print(f"{name}在{i + 1}点唱歌！")
    time.sleep(0.1)
    thread = threading.current_thread()
    print(thread)
    return None
def dance(name,num):
    """
    :param name:
    :param num:
    :return:
    """
    for i in range(num):
        print(f"{name}同学在星期{i + 1}唱歌！")
    thread = threading.current_thread()
    print(thread.name)
    time.sleep(0.1)
    return None

if __name__ == '__main__':
    time.sleep(0.2)
    print("主线程结束")
    # 创建线程对象
    sing_thread = threading.Thread(target=sing, args=("Bob", 3,))
    # 设置守护主线程
    sing_thread.daemon = True
    sing_thread.start()

    dance_thread = threading.Thread(target=dance, kwargs={"name": '张三', 'num': 3})
    dance_thread.daemon = True
    dance_thread.start()

    # sing_thread = threading.Thread(target=sing, args=("Bob", 3,), daemon=True)
    # sing_thread.start()

    # dance_thread = threading.Thread(target=dance, kwargs={"name": '张三', 'num': 3}, daemon=True)
    # dance_thread.start()

    # 多线程任务之间的执行是无序的

