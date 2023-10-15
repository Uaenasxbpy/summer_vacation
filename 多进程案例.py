# 高并发的拷贝器
import os
import multiprocessing
def copy_file(file_name,source_dir,dest_dir):
    """
    实现文件拷贝
    :return:
    """
    # 拼接源文件路径和目标文件路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name

    # 打开源文件和目标文件
    with open(source_path,"rb") as source_file:
        with open(dest_path,"wb") as dest_file:
            while(True):
                data = source_file.read(1024)
                if(data):
                    dest_file.write(data)
                else:
                    break
    # 循环读取源文件到目标文件
    return None

if __name__ == '__main__':
    # 定义源文件夹和目标文件夹
    source_dir = "数据文件"
    dest_dir = "dest"

    # 创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在！")

    # 读取源文件夹的文件列表
    file_list = os.listdir(source_dir)
    # print(file_list)

    # 遍历文件列表实现拷贝 -- 单任务
    for file_name in file_list:
        copy_file(file_name,source_dir,dest_dir)

    # 使用多进程任务拷贝
    sub_process = multiprocessing.Process(target=copy_file,args=(file_name,source_dir,dest_dir,))
    sub_process.start()