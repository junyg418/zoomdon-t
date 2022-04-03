from datetime import datetime
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import SystemModul
import a_3
import SubEditerModul
'''
    -widget 왼쪽에 table, 오른쪽에 현상황 띄어주자
        현상황에 시간, 대기중인지 아닌지, 지금은 몇교시인지 크게크게
    -table head 교시,월,화,수,목,금 으로 변경
    -설정버튼추가

    -rowcount가 nan일떄 정수로 변환하지 못해 발생하는 버그
        데이터를 입력하지 않고 시켰을 떄 
'''

class MainA_2(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.setGeometry(0,0,1024,768)
        self.setFixedSize(1024, 768)
        self.mainwidget()

    def mainwidget(self):
        self.main_a2lay = QGridLayout()
        self.main_a2lay.setRowStretch(0, 1)
        self.main_a2lay.setRowStretch(1, 5)
        self.main_a2lay.setColumnStretch(0, 2)
        self.main_a2lay.setColumnStretch(1, 1)
        self.setLayout(self.main_a2lay)



        self.top_a2lay = QGridLayout()
        self.top_a2lay.setColumnStretch(1, 1)
        self.main_a2lay.addLayout(self.top_a2lay, 0, 0, 1, 2)

        self.onoff_a2btn = QPushButton('on')      #토글 on off버튼으로 변경해야함 
        self.top_a2lay.addWidget(self.onoff_a2btn, 0, 0)
        
        self.pageEdit_a2btn = QPushButton('초기화')
        self.pageEdit_a2btn.clicked.connect(self.to_setting)
        self.top_a2lay.addWidget(self.pageEdit_a2btn, 0, 2)
        
        self.setting_a2btn = QPushButton('설정')
        self.top_a2lay.addWidget(self.setting_a2btn, 0, 3)
        
        self.infoPage = QGridLayout()    #오른쪽 레이아웃
        self.main_a2lay.addLayout(self.infoPage, 1, 1)
        self.lin = QLineEdit()
        self.infoPage.addWidget(self.lin, 0 ,0)
        
        self.timer = QtCore.QTimer()
        self.timer.start(1000*60)
        self.timer.timeout.connect(self.settimer)


        self.bot_a2lay = QGridLayout()
        self.main_a2lay.addLayout(self.bot_a2lay, 1, 0)
        self.showSigan_a2table = QTableWidget()                           #시간표 Tablewidget 설정
        self.showSigan_a2table.setColumnCount(6)
        self.showSigan_a2table.verticalHeader().setVisible(False)
        column_headers = ['시간/요일', '월', '화', '수', '목', '금']
        self.showSigan_a2table.setHorizontalHeaderLabels(column_headers)
        self.tableRowcount = SubEditerModul.getMaximumvalue()
        self.showSigan_a2table.setRowCount(int(self.tableRowcount))
        self.table_height = self.showSigan_a2table.height()
        self.table_width = self.showSigan_a2table.width()
        for row_count in range(self.showSigan_a2table.rowCount()):
            self.showSigan_a2table.setRowHeight(row_count, 75)
        self.showSigan_a2table.setColumnWidth(0, 100)
        for column_count in range(1, self.showSigan_a2table.columnCount()):
            self.showSigan_a2table.setColumnWidth(column_count, self.table_width//8+20)
        self.bot_a2lay.addWidget(self.showSigan_a2table)
        self.settingtableWidget()

    def settimer(self):
        sender = self.sender()
        currentTime = QtCore.QTime.currentTime().toString("hh:mm")
        if id(sender) == id(self.timer):
            # print(currentTime)   #시간정보 출력
            today = datetime.today().weekday()
            sjtDic = SubEditerModul.Nameslist(SubEditerModul.searchSortsjt(today+1))
            if SubEditerModul.currentCheck(currentTime):
                sjt_name = sjtDic[int(SubEditerModul.returnTimeIndex(currentTime))]
                # sjtDic[(SubEditerModul.returnTimeIndex(currentTime))]   /ex
                SystemModul.linkget(SubEditerModul.NameLinktoDic(SubEditerModul.get_NametoLink(sjt_name))[sjt_name])

    def settingtableWidget(self):
        # print(self.showSigan_a2table.rowCount())
        for column in range (1, 6):
            if str(SubEditerModul.getDayMaximum(column)) == 'nan':
                self.showSigan_a2table.setItem(0, column, QTableWidgetItem('시간표가 설정되지 않았습니다'))
            else:    
                for row in range(0, int(SubEditerModul.getDayMaximum(column))):
                    # print(SubEditerModul.Nameslist(SubEditerModul.searchSortsjt(column))[row+1])
                    text = SubEditerModul.Nameslist(SubEditerModul.searchSortsjt(column))[row+1]
                    if text == 0:
                        self.showSigan_a2table.setItem(row, column, QTableWidgetItem('       X'))
                    else:
                        self.showSigan_a2table.setItem(row, column, QTableWidgetItem(text))

    def to_setting(self):
        self.a_3_info = a_3.EditInterface()
        self.a_3_info.show()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainA_2()
    ex.show()
    sys.exit(app.exec_())