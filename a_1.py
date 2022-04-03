from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import Qt
import csv
import pandas as pd
import sys
import SubEditerModul
import a_2
import a_3

'''
메모
    -a_1에서 수정버튼 작동 안함
        a_3에서 수정기능 지원 but 수정하면 오류나는듯? -> a_1의 수정기능 삭제?
    -a_1에서 과목삭제버튼 추가하면 좋을듯
    -a_1의 +버튼 길이 너무 길다
    -a_2의 tablewidget의 rowCount 어떻게 설정
    -a_3에서 과목추가버튼 추가하면 좋을듯
        주석처리됨
    -a_3의 경고창 수정해야함
    -a_3의 리셋함수 꺼둠
    -SubEditerModul에서 과목명과 링크를 딕셔너리로 받아 SystemModul 에서 실행시키면 될듯
    -Zoom 접속시 초기에 나타나는 쿠키정보 허용버튼 어떻게 누르게 하지
    -컴퓨터 키자마자 프로그램 자동실행,프로그램을 닫아도 백그라운드에서 작동기능 추가하면 좋을듯


확인된 버그
    -a_3에서 왼쪽 과목명들을 바꿔도 commbobox의 item의 명이 바뀌지 않는버그
        과목명 바꾸고 combobox를 선택하면 오류 새로고침 해야하나?
        새로 만드는row에서는 적용 but 이미 만들어진 row에서는 바뀌지 않음
    -a_3에서 같은 요일에 중복되는 과목이 있으면 나중시간으로 데이터가 저장되는 버그
        for문 위에서 아래 왼쪽에서 오른쪽으로 데이터를 읽기에 나는 오류
    -a_3에서 아무것도 선택하지 않았을떄 오류남
        일단 주석처리로 해결
'''


# def skip_a_2():
#     a = a_2.MainA_2()
#     a.show()


sjnum = 2
class LinkAccepting(QWidget):
    def __init__(self):
        super().__init__()
        # self.setGeometry(0,0,1024,768)
        self.setFixedSize(1024, 768)
        if SubEditerModul.a_1Check() == True:
            self.to_a_2()
        else:  
            self.info()
            self.show()



    def info(self):
        self.Main_Haslay = QGridLayout()           #Main_Haslay구성
        self.setLayout(self.Main_Haslay)


        self.top_Haslay = QHBoxLayout()
        self.Main_Haslay.setRowStretch(0, 1)
        self.Main_Haslay.addLayout(self.top_Haslay, 0, 0)        #toplay
        
        self.Hason_Title = QLabel('<과목별 줌 주소 입력>')#334
        self.Hason_Title.setStyleSheet('''  font : 맑은 고딕;
                                            font-size: 30px;
                                            color: #000000;
                                            font-weight: 500;''')
        self.top_Haslay.addStretch(1)
        self.top_Haslay.addWidget(self.Hason_Title)
        self.top_Haslay.addStretch(1)



        self.Mid_Haslay = QVBoxLayout()                                  #midlay
        self.Main_Haslay.setRowStretch(1, 4)
        self.Main_Haslay.addLayout(self.Mid_Haslay, 1, 0)

        self.sjt_HasScroll = QScrollArea()
        self.Mid_Haslay.addWidget(self.sjt_HasScroll)

        self.sjtEdit_Widget = QWidget()
        self.sjt_HasScroll.setWidget(self.sjtEdit_Widget)
        self.sjt_HasScroll.setWidgetResizable(True)

        global sjtEdit_lay
        sjtEdit_lay = QVBoxLayout()
        self.sjtEdit_Widget.setLayout(sjtEdit_lay)

        self.sjt_1lay = SubjectManajment()

        self.addSub_lay = QHBoxLayout()
        self.addSub_btn = QPushButton("+")
        self.addSub_btn.clicked.connect(self.input_to_lay)
        # self.addSub_btn.clicked.connect(self.to_a_2)
        
        self.addSub_lay.addWidget(self.addSub_btn)
        self.Mid_Haslay.addLayout(self.addSub_lay)
        # self.Mid_Haslay.setRowMinimumHeight0
        


        self.Bot_Haslay = QHBoxLayout() 
        self.Main_Haslay.setRowStretch(2, 1)
        self.iamok_btn = QPushButton('OK')
        self.iamok_btn.clicked.connect(self.to_a_3)
        self.iamok_btn.clicked.connect(SubEditerModul.a_1Accept)
        self.Bot_Haslay.addStretch(1)
        self.Bot_Haslay.addWidget(self.iamok_btn)
        self.Main_Haslay.addLayout(self.Bot_Haslay, 2, 0)


    def send_to_local1(self):
        with open('subject_data.csv', mode='a', encoding='utf-8', newline='') as sjdata:
            wr = csv.writer(sjdata)
            wr.writerow([self.sjtName_1le.text(),self.sjtLink_1le.text()])
            sjdata.close()
        self.sjtEnter_1btn.hide()
        self.sjtEdit_1btn.show()
        self.sjtName_1le.setReadOnly(True)
        self.sjtLink_1le.setReadOnly(True)

    def input_to_lay(self):
        global sjnum
        globals()[f'sjt_{sjnum}lay'] = SubjectManajment()
        sjnum += 1

    def to_a_2(self):
        self.a_2go = a_2.MainA_2()
        self.a_2go.show()
        self.hide()

    def to_a_3(self):
        self.a_3go = a_3.EditInterface()
        self.a_3go.show()
        self.close()


class SubjectManajment:
    def __init__(self) -> None:
        self.make_sj = QGridLayout()
        sjtEdit_lay.addLayout(self.make_sj)


        self.Name_Ld = QLineEdit('과목')
        self.make_sj.addWidget(self.Name_Ld, 0, 0)
        self.make_sj.setColumnStretch(0, 1)
        self.Link_Ld = QLineEdit('링크')
        self.make_sj.setColumnStretch(1, 3)
        self.make_sj.addWidget(self.Link_Ld, 0, 1)
        self.Enter_btn = QPushButton('확인')
        self.Enter_btn.clicked.connect(self.send_to_local)
        self.make_sj.addWidget(self.Enter_btn, 0, 2)
        self.Edit_btn = QPushButton('수정')
        # self.Edit_btn.clicked.connect(self.editEnter)
        self.Edit_btn.hide()
        self.make_sj.addWidget(self.Edit_btn, 0, 2)

    def send_to_local(self):
        with open('./csv_files/subject_data.csv', mode='a', encoding='utf-8', newline='') as sjdata:
            wr = csv.writer(sjdata)
            wr.writerow([self.Name_Ld.text(),self.Link_Ld.text()])
            sjdata.close()
        self.Enter_btn.hide()
        self.Edit_btn.show()
        self.Name_Ld.setReadOnly(True)
        self.Link_Ld.setReadOnly(True)

    # def editEnter(self):
    #     self.subjectdata = pd.read_csv('subject_data.csv',names=['sj_Name','sj_Link','Mon','Tus','Wed','Thr','Fri','Sat','Sun'])
    #     # self.subjectdata.drop(self.subjectdata['sj_Name'] == self.Name_Ld.text(), axis= 0)
    #     self.subjectdata.drop(self.subjectdata['sj_Name'] == '과목', axis= 0)
    #     self.Name_Ld.setReadOnly(False)
    #     self.Link_Ld.setReadOnly(False)
    #     self.Enter_btn.show()
    #     self.Edit_btn.hide()

        # subjectdata.drop(((subjectdata['sj_Name'] == self.Name_Ld.text()) & (subjectdata['sj_Link'] == self.Link_Ld.text())).index)


    # def deleat_sj(self):
        # sjtEdit_lay.




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LinkAccepting()
    # ex.show()
    sys.exit(app.exec_())

