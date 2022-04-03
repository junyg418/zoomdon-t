from os import name
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import time
import csv
import SubEditerModul
import pandas as pd
import a_2


i = 0
whattime = 1

class EditInterface(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.setGeometry(0,0,1024,768)
        self.setFixedSize(1024, 768)
        
        self.Editinfo()

    def Editinfo(self):
        self.MainEdit_Eunlay = QGridLayout()
        self.setLayout(self.MainEdit_Eunlay)
        
        self.under_lay = QGridLayout()
        self.MainEdit_Eunlay.addLayout(self.under_lay, 1, 0, 2, 0)
        self.under_lay.setColumnStretch(0, 8)
        self.under_lay.setColumnStretch(1, 1)


        self.undercheck_Btn = QPushButton('저장')
        self.undercheck_Btn.released.connect(self.resetData)
        self.undercheck_Btn.released.connect(self.acceptEntertimedata)
        self.under_lay.addWidget(self.undercheck_Btn, 0, 1)

        self.EditLeft_Eunlay = QVBoxLayout()                                #왼쪽 레이아웃
        self.MainEdit_Eunlay.addLayout(self.EditLeft_Eunlay, 0, 0)
        self.MainEdit_Eunlay.setColumnStretch(0, 1)
        self.MainEdit_Eunlay.setColumnStretch(1, 5)
        
        self.sjtList_Sc = QScrollArea()
        self.sjtList_Sc.setWidgetResizable(True)
        self.EditLeft_Eunlay.addWidget(self.sjtList_Sc)

        self.scrollwidget = QWidget()
        self.sjtList_Sc.setWidget(self.scrollwidget)
        self.sjtList_lay = QVBoxLayout()
        self.sjtList_lay.setAlignment(Qt.AlignTop)
        self.scrollwidget.setLayout(self.sjtList_lay)

        self.EditRight_Eunlay = QGridLayout()                                #오른쪽 레이아웃
        self.MainEdit_Eunlay.addLayout(self.EditRight_Eunlay, 0, 1)
        self.addSjtEdit()


        # self.row_int = 1
        global siganpyo_Tablewidget
        siganpyo_Tablewidget = QTableWidget()
        siganpyo_Tablewidget.setColumnCount(6)
        siganpyo_Tablewidget.setRowCount(1)
        siganpyo_Tablewidget.setRowHeight(0,75)
        siganpyo_Tablewidget.verticalHeader().setVisible(False)
        global width
        width = siganpyo_Tablewidget.width()
        siganpyo_Tablewidget.setColumnWidth(0, width//5)
        for i in range(1,8):
            siganpyo_Tablewidget.setColumnWidth(i, width//6+14)
        # siganpyo_Tablewidget.setRowHeight()
        self.EditRight_Eunlay.addWidget(siganpyo_Tablewidget)

        
        column_headers = ['시간/요일', '월', '화', '수', '목', '금']
        siganpyo_Tablewidget.setHorizontalHeaderLabels(column_headers)
        # siganpyo_Tablewidget.header

        self.plus_btn = QPushButton('+')
        self.plus_btn.clicked.connect(self.addPlusRow)
        siganpyo_Tablewidget.setCellWidget(siganpyo_Tablewidget.rowCount()-1, 0, self.plus_btn)




    def addPlusRow(self):    #행 추가 버튼
        self.lastRow = siganpyo_Tablewidget.rowCount()
        siganpyo_Tablewidget.insertRow(self.lastRow)
        siganpyo_Tablewidget.setRowHeight(self.lastRow, 75)
        siganpyo_Tablewidget.removeCellWidget(self.lastRow-1, 0)
        self.addNewplusbtn()
        self.addTimeInfo()

    def addNewplusbtn(self):    #+버튼 갱신함수
        plus_btn = QPushButton('+')
        plus_btn.clicked.connect(self.addPlusRow)
        siganpyo_Tablewidget.setCellWidget(self.lastRow, 0 ,plus_btn)

    def addTimeInfo(self):    #시간설정 widget 추가
        global whattime
        siganpyo_Tablewidget.setCellWidget(self.lastRow-1, 0, SendToInfoEdit(whattime))
        whattime += 1
        self.addsjtCombo()

    def addsjtCombo(self):    #combobox 추가
        # print(siganpyo_Tablewidget.cellWidget(0,0).get_time())
        for column in range(1,siganpyo_Tablewidget.columnCount()):
            siganpyo_Tablewidget.setCellWidget(siganpyo_Tablewidget.rowCount()-2, column, ComboBoxInfoEdit())

    def addSjtEdit(self):     #왼쪽 위젯들 추가함수
        for Name in SubEditerModul.namesCheck():
            self.sjtList_lay.addWidget(SjtButtonInfo(Name))

    def acceptEntertimedata(self):   #시간데이터 저장
        SubEditerModul.timeDataReset()
        for row in range(siganpyo_Tablewidget.rowCount()-1):
            siganpyo_Tablewidget.cellWidget(row, 0).addTimeData(row+1)


    def resetData(self):
        SubEditerModul.reset_sjtdata()
        self.sjtDayInfoAdding()

    def sjtDayInfoAdding(self):  #과목data에 요일추가 /저장버튼눌렀을 때
        for column in range(1,siganpyo_Tablewidget.columnCount()):
            for row in range(siganpyo_Tablewidget.rowCount()):
                # print(siganpyo_Tablewidget.cellWidget(row, column))
                if siganpyo_Tablewidget.cellWidget(row, column) == None:
                    continue
            
                else:
                    SubEditerModul.sjtyoiladding(siganpyo_Tablewidget.cellWidget(row,column).returnText(), str(column), str(row+1))
        SubEditerModul.Save()
        self.SaveMaximumRow()

    def SaveMaximumRow(self):    #실험중
        # print(SubEditerModul.getMaximumvalue())
        if str(SubEditerModul.getMaximumvalue()) == 'nan':  #값에 아무것도 없을 떄
            self.warningOpen() #경고창 발행
        else:
            # print('성')
            self.goto_a_2()

    def warningOpen(self):
        self.warning = WarningMessage()

    def goto_a_2(self):
        self.go_a_2 = a_2.MainA_2()  
        self.go_a_2.show()
        self.close()


class WarningMessage(QDialog):
    def __init__(self) -> QDialog:
        super().__init__()
        self.setWindowTitle('경고창')
        self.setWindowModality(2)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.acceptbutton = QPushButton('확인')
        self.acceptbutton.released.connect(self.closeWarning)
        self.text_Lb = QLabel('시간표를 설정하지 않았습니다')
        
        self.layout.addWidget(self.text_Lb, 0, 0)
        self.layout.addWidget(self.acceptbutton, 1, 0)
        self.show()

    def closeWarning(self):
        self.close()


class SendToInfoEdit(QWidget):
    def __init__(self, time):
        super().__init__()
        layout = QVBoxLayout()

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.LineEdit= QLineEdit(f'{time}교시')
        layout.addWidget(self.LineEdit)

        self.timeeidt = QTimeEdit()
        self.timeeidt.setDisplayFormat('hh시mm분')
        layout.addWidget(self.timeeidt)
        self.setLayout(layout)

    def getTime(self,time):
        self.Timelist = [time,self.LineEdit.text() , f'{self.timeeidt.time().hour()}:{self.timeeidt.time().minute()}']
        return self.Timelist

    def addTimeData(self,time):
        timeData = pd.read_csv('./csv_files/sjt_timeInfoData.csv', names=['names', 'times'])
        if timeData.empty:
            with open('./csv_files/sjt_timeInfoData.csv', mode='w', encoding='utf-8', newline='') as sjtimedata:
                wr = csv.writer(sjtimedata)
                wr.writerow(self.getTime(time))
                sjtimedata.close()
        else:
            with open('./csv_files/sjt_timeInfoData.csv', mode='a', encoding='utf-8', newline='') as sjtimedata:
                wr = csv.writer(sjtimedata)
                wr.writerow(self.getTime(time))
                sjtimedata.close()


class ComboBoxInfoEdit(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem('없음')
        self.get_sjtinfo()

    def returnText(self):
        return self.currentText()
        # print(self.currentText())

    def get_sjtinfo(self):
        self.addItems(SubEditerModul.namesCheck())


class SjtButtonInfo(QPushButton):
    def __init__(self, sjtName)->QPushButton:
        super().__init__()
        self.setText(str(sjtName))
        self.clicked.connect(self.EditPageOpen)

    def EditPageOpen(self):
        self.EditPage = SjtEditWidget(str(self.text()))
        self.EditPage.AcceptBtn.pressed.connect(self.EditPage.getNameAndLink)
        self.EditPage.AcceptBtn.pressed.connect(self.changeName)

    def changeName(self):
        self.setText(str(self.EditPage.name))
        self.EditPage.AcceptBtn.released.connect(self.EditPage.closeAndSave)


class SjtEditWidget(QDialog):
    def __init__(self, Name)->QDialog:
        super().__init__()
        self.Button_text = Name
        self.setWindowTitle(Name)
        self.setWindowModality(2)
        self.MainLay = QGridLayout()

        self.NameLineEidt = QLineEdit()
        self.NameLineEidt.setText(Name)
        self.LinkLineEdit = QLineEdit()
        self.Link = SubEditerModul.NameLinktoDic(SubEditerModul.get_NametoLink(Name))[Name]
        self.LinkLineEdit.setText(str(self.Link))
        self.AcceptBtn = QPushButton('확인')
        # self.AcceptBtn.released.connect(lambda:self.closeAndSave)


        self.setLayout(self.MainLay)
        self.MainLay.addWidget(self.NameLineEidt, 0, 0)
        self.MainLay.addWidget(self.AcceptBtn, 0, 1)
        self.MainLay.addWidget(self.LinkLineEdit, 1, 0, 1, 2)
        self.show()

    def getNameAndLink(self):
        self.name = str(self.NameLineEidt.text())
        self.link = str(self.LinkLineEdit.text())


    def closeAndSave(self):
        SubEditerModul.resetSjtInfo(self.Button_text, self.name, self.link)
        # SjtButtonInfo(self.Button_text).setText(self.name)    #이거시 문제로우다
        # print(SjtButtonInfo(self.Button_text).text())
        # # print(self.Button_text)
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EditInterface()
    ex.show()
    # ex = SjtEditWidget('독서')
    # ex.show()
    sys.exit(app.exec_())
