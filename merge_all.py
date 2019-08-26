import os
import pandas as pd

def merge(read_path,save_path):
    catelist=os.listdir(read_path)
    for file in catelist:
        data=pd.read_csv(save_path+file)
        data=data.append(pd.read_csv(read_path+file))
        if 'category' not in data.columns:
            columns=['title','content']
            data=data[columns]
        else:
            columns=['title','content','category']
            data=data[columns]
        # data=data.dropna(how='any')
        print('{}文件有{}条数据'.format(file,len(data)))
        data.to_csv(save_path+file,index=False)

if __name__=='__main__':
    merge('D:/spider/total0729/','D:/spider/total/')

## 总数
# ershou.csv文件有2547条数据            7733
# newcar.csv文件有46466条数据           106437
# newEnergy.csv文件有18543条数据         27066
# news.csv文件有200294条数据             133487
# selection.csv文件有33783条数据         34577

newcar=pd.read_csv(r'D:\spider\total\newcar.csv')
news=pd.read_csv(r'D:\spider\total\news.csv')
newcar=newcar.append(news[news['category'].isin(['进口新车','国产新车','新车图解'])])
newcar=newcar.append(news[news['title'].str.contains('新车')])

news=news[~news['category'].isin(['进口新车','国产新车','新车图解'])]
news=news[~news['title'].str.contains('新车')]

news=news[~news['category'].isin(['新能源'])]
news=news[~news['title'].str.contains('新能源')]
news=news[~news['title'].str.contains('二手')]
news=news[~news['title'].str.contains('选车')]
news=news[~news['title'].str.contains('试驾')]