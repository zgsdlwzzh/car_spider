import pandas as pd
import os


def mergedata(read_path,save_path):
    catelist = os.listdir(read_path)  ## 获取read_path下所有子目录
    for file in catelist:  ## 文件夹下的子文件夹名
        merge = pd.DataFrame()
        class_path = read_path + file + '/'  ## 子文件夹路径
        file_list = os.listdir(class_path)  ## 获取子文件夹下所有的文件
        for file_path in file_list:
            fullname = class_path + file_path  ## 所有文件的子路径
            data=pd.read_csv(fullname,encoding='utf-8')
            merge=merge.append(data)
        num=len(merge)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        if 'category' not in merge.columns:
            columns=['title','content','publish_time']
            merge=merge[columns]
        else:
            columns = ['title', 'content', 'category', 'publish_time']
            merge = merge[columns]
        merge.to_csv(save_path+file+'.csv',index=False,encoding='utf-8')
        print('{} 类别有{}条数据'.format(file,num))

if __name__=='__main__':
    mergedata('C:/Users/lenovo/Desktop/spider/cleaned0729/','C:/Users/lenovo/Desktop/spider/total0729/')




