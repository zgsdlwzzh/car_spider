import pandas as pd
import os

def progress(filename):
    data=pd.read_csv(filename,header=0)
    data=data.dropna(how='any')
    data=data.drop_duplicates()
    data=data.reset_index(drop=True)
    for i in range(len(data)):
        data['title'][i]=data['title'][i].replace('\n','').replace('\r','').replace(' ','').replace('\u3000','').replace('\xa0','').replace('\t','')
        data['content'][i]=data['content'][i].replace('\n','').replace('\r','').replace(' ','').replace('\u3000','').replace('\xa0','').replace('\t','')
    data=data.dropna(how='any')
    data=data.drop_duplicates()
    data=data.reset_index(drop=True)
    return data

def read_and_save(read_path,save_path):
    catelist=os.listdir(read_path)                 ## 获取read_path下所有子目录
    for file in catelist:                          ## 文件夹下的子文件夹名
        class_path=read_path+file+'/'              ## 子文件夹路径
        save_dir=save_path+file+'/'                ## 处理后存储的文件路径
        if not os.path.exists(save_dir):           ## 若不存在则创建该目录
            os.makedirs(save_dir)

        file_list=os.listdir(class_path)           ## 获取子文件夹下所有的文件
        for file_path in file_list:
            fullname=class_path+file_path          ## 所有文件的子路径
            cleaned_data=progress(fullname)        ## 数据清洗
            cleaned_data.to_csv(save_dir+file_path,index=False,encoding='utf-8')

if __name__=='__main__':
    read_path='C:/Users/lenovo/Desktop/spider/data0729/'
    save_path='C:/Users/lenovo/Desktop/spider/cleaned0729/'
    read_and_save(read_path,save_path)

#-----------------------------------------------------------------------------------------------
# data=pd.read_csv(r'C:\Users\lenovo\Desktop\spider\cleaned\ershou\cyol_ershou.csv')
# data=data.drop_duplicates(subset=['title'])
# data=data.dropna(how='any')
# data=data.reset_index(drop=True)
# data.to_csv(r'C:\Users\lenovo\Desktop\spider\cleaned\ershou\cyol_ershou.csv',index=False)
#
# data=pd.read_csv(r'C:\Users\lenovo\Desktop\spider\cleaned\newEnergy\cyol_newenergy.csv')
# data=data.drop_duplicates(subset=['title'])
# data=data.dropna(how='any')
# data=data.reset_index(drop=True)
# data.to_csv(r'C:\Users\lenovo\Desktop\spider\cleaned\newEnergy\cyol_newenergy.csv',index=False)


