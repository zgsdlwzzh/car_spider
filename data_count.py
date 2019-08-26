import pandas as pd
import os

## 统计清洗后数量
def countdata(read_path):
    catelist = os.listdir(read_path)  ## 获取read_path下所有子目录
    for file in catelist:  ## 文件夹下的子文件夹名
        num=0
        class_path = read_path + file + '/'  ## 子文件夹路径
        file_list = os.listdir(class_path)  ## 获取子文件夹下所有的文件
        for file_path in file_list:
            fullname = class_path + file_path  ## 所有文件的子路径
            data=pd.read_csv(fullname,encoding='utf-8')
            num+=len(data)
        print('{} 类别有{}条数据'.format(file,num))

if __name__=='__main__':
    countdata('C:/Users/lenovo/Desktop/spider/cleaned0729/')

# ershou 类别有1393条数据
# newcar 类别有25898条数据
# newEnergy 类别有13943条数据
# news 类别有180093条数据
# selection 类别有25581条数据
# 总 246908


