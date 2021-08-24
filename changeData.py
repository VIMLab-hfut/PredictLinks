# -*- codeing = utf-8 -*-
# @Time : 2021/8/17 10:32
# @Author : MC
# @File : changeData.py
# @Software : PyCharm


import pandas as pd


def change_data(source_path = '.../raw_data/test.csv',save_path = '..../raw_data/dev100.txt'):
    # 将数据集中的数据做筛选处理，使得剩余的数据量满足程序运行的内存限制
    edge_data = pd.read_csv(source_path)
    with open(save_path,'w') as f:
        for edge in edge_data.values:
            # if(int(edge[0]) <= 5000 and int(edge[1]) <= 5000):
            if(0 < int(edge[0])-int(edge[1]) < 100 or 0 < int(edge[1])-int(edge[0]) < 100):
                # print(int(edge[0]),int(edge[1]))
                f.write("%s\n" % (str(edge[0])+" "+str(edge[1])))


if __name__ == '__main__':
    change_data()