from datetime import datetime
from typing import List
from numpy import mod, product
import pandas as pd
import csv

from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv

subfile = pd.read_csv('./csv_files/subject_data.csv')


def namesCheck()->list: #이름 리스트화 함수
    return list(subfile['Names'])

def get_NametoLink(Name)->DataFrame: #이름 column 추출 함수
    # print(subfile[subfile['Names']==Name])
    return subfile[subfile['Names']==Name]                  #for i in namesCheck(): getNametoLink(i)  형식으로 사용 

def NameLinktoDic(DataFrame)->dict:  #함수 딕셔너리화
    Dic = {DataFrame.iloc[0,0]:DataFrame.iloc[0,1]}
    return Dic



def resetSjtInfo(first_Name, Name, Link):                                                          #위 아래함수 묶음
    subfile.loc[(subfile.Names == first_Name), 'Links'] = Link                                    #QDialog 과목 변경 함수
    
    subfile.to_csv('./csv_files/subject_data.csv', mode='w', encoding='UTF-8', index=False)
    namechange(first_Name, Name)

def namechange(first_Name, Name): 
    subfile.loc[(subfile.Names == first_Name), 'Names'] = Name
    subfile.to_csv('./csv_files/subject_data.csv', mode='w', encoding='UTF-8', index=False)


def sjtyoiladding(sjtName, day, time):   #과목datafram에 시간data 추가
    subfile.loc[(subfile.Names == sjtName), day] = time
    subfile.to_csv('./csv_files/subject_data.csv', mode='w', encoding='UTF-8', index=False)


def getMaximumvalue()->int:   #과목 최대 시간 return
    maxi = pd.read_csv('./csv_files/subject_data.csv')
    return maxi[['1','2','3','4','5']].max(axis=0).max(axis=0)

def getDayMaximum(day)->int:
    maxi = pd.read_csv('./csv_files/subject_data.csv')
    return maxi[str(day)].max(axis=0)

def reset_sjtdata(): #과목데이터 초기화 a_2에서사용
    global subfile
    subfile.drop(['1','2','3','4','5'], axis=1, inplace = True)
    subfile['1'] = None
    subfile['2'] = None
    subfile['3'] = None
    subfile['4'] = None
    subfile['5'] = None
    # subfile.columns = ['Names','Links','1','2','3','4','5']
    subfile.to_csv('./csv_files/subject_data.csv', mode='w', encoding='UTF-8', index=False)

def searchSortsjt(day):
    if day == 1:
        column = subfile['1']
    elif day == 2:
        column = subfile['2']
    elif day == 3:
        column = subfile['3']
    elif day == 4:
        column = subfile['4']
    elif day == 5 :
        column = subfile['5']
    return column

def Nameslist(column)->dict:  #위 함수와 같이 쓰임 ex)Nameslist(searchSortsjt(1,2,3,4,5))
    NameDic = {}
    if column.dropna().empty:
        return NameDic
        
    else:
        for i in range(1, int(column.max())+1): #day의 maxmum
            if subfile.loc[column == i].empty:
                NameDic[i] = 0
            else:
                # print(i)
                # print(subfile.loc[column == i].iloc[0, 0])
                # print()
                NameDic[i] = subfile.loc[(column ==i)].iloc[0, 0]
        return NameDic
        # print(type(subfile.loc[column == 6]))

    
def Save():
    return subfile.to_csv('./csv_files/subject_data.csv', mode='w', encoding='UTF-8', index=False)
            

def printDf():
    return print(subfile)


timeData = pd.read_csv('./csv_files/sjt_timeInfoData.csv', names=['indexs', 'names', 'times'])

def currentCheck(currenttime):
    if currenttime in timeData['times'].values:
        return True
    # time.iloc[0,]
# def TimeList(column):
#     list = []
#     for i in range(1, int(column.max())+1):
#         print(subfile.loc[column == i])
#         # if subfile.loc[column == i].empty:
#         #     # continue
#         # else:
#         #     pass
def returnTimeIndex(currenttime):
    return timeData.loc[(timeData.times == currenttime)].iloc[0, 0]

def TimeList()->list:
    pass

def timeDataReset():
    if timeData.empty:
        pass
    else:
        timeData.drop(columns=['indexs', 'names', 'times'], axis=1, inplace=True)
        timeData.to_csv('./csv_files/sjt_timeInfoData.csv', mode='w', encoding='UTF-8', index=False)




infodata = pd.read_csv('./csv_files/info_data.csv')

def a_1Check(): #bool 바꾸기ㅣ
    if infodata.iloc[0, 1] == 'True':
        return True
    if infodata.iloc[0, 1] == 'False':
        a_1Accept()

def a_1Accept():  #a_1두번째 방문시 열리지 않게 설정
    infodata.iloc[0, 1] = 'True'
    infodata.to_csv('./csv_files/info_data.csv', mode='w', index=False)

def a_3returnRow()->int:    #로우값 추출   #a_3의 row값 defult = 1
    return int(infodata.iloc[1, 1])


if __name__ == '__main__':
    print(NameLinktoDic(get_NametoLink('국어'))['국어'])
    # print({1: '국어'}[int(returnTimeIndex('12:33'))])
