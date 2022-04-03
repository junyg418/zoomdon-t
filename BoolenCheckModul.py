import pandas as pd

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

# def a_3rowSave(row):   #a_3의 row값을 저장
#     df.iloc[1,1] = row
#     df.to_csv('./csv_files/info_data.csv', mode='w', index=False)






if __name__ == '__main__':
    subfile = pd.read_csv('./csv_files/sjt_timeInfoData.csv', names=['Times','infos'])
    print(subfile.loc[(subfile.Times == 1)].iloc[0,1][1])
