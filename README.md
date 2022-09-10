# zoomdon-t
줌에 자동으로 들어가게 해주는 플레너 앱  
2021-07-02 ~ 2021-11-06  제작  
제작한지 너무 오래됨 -> 코드 리워크 예정

## csv_file (folder)  
### info_data.csv
a_1 page(첫 초기 설정 페이지)가 처음만 나오게 하기 위한 파일  

### sjt_timeInfoData.csv
각각의 교시의 시작 시간을 저장하는 csv 파일
a_3 page(스케쥴 설정 페이지) 에서 데이터 입력 후 로컬 저장하기 위하여  
파일 제작  

### subject_data.csv  
##### pandas 모듈 사용  
과목들의 과목별 정보를 저장   
head 과목명, 링크, 요일별 몇교시인지  
요일별 교시는 1,2,3,4,5 형태로 "월화수목금" 을 나타내고  
각 하위 데이터에는 정수형태로 교시의 수를 나타낸다.  

## BoolenCheckModul.py
##### pandas 모듈 사용
csv_file\info_data.csv 의 파일을 능동적으로 수정하기 위하여  
작성한 모듈  

## SubEditerModul.py
##### pandas 모듈 사용
여러 데이터들을 수정 및 연산 처리  
데이터 저장, 데이터 불러오기 등 여러 데이터 처리 모듈  

## SystemModul.py
##### selenium 모듈 사용 
csv_file\subject_data.csv 파일에 있는 링크에 접속하기 위한 모듈  
이를 만드는 과정 중 힘들었던 점    
- zoom링크에 접속시 경고창이 떴었기에  
  이를 자동화 하기 위하여 cookie를 자동 할당하는 코드 작성  
  but cookie를 할당하기에 cookie 값을 찾을 수 없었음  
so 이를 해결하기 위해 계속 실행될 때 마다의 초기화 되는 사용자 데이터를  
  로컬 데이터로 사용자 데이터를 저장하도록 하여   
  쿠키 데이터를 처음만 수락 하게 되면 그 뒤로는 자동적으로 바로 접속되게 하였다.  
  
# GUI 프로그래밍
##### PyQt5 모듈 사용, GUI 제작

## a_1.py
초기 입력 정보를 받기 위한 GUI
과목명, 과목의 링크를 받아 subject_data.csv에 저장함  
> __class LinkAccepting__
>> 주소를 입력하기 위한 GUI 
>> QWidget 상속 클레스

> __class SubjectManajment__  
>> 주소를 입력하기 위한 입력칸 

## a_2.py  
화상채팅에 들어가기 위한 대기하고있는 __실질적 작동 GUI__  
subject_data.csv 에 있는 데이터를 받아 시간표와 같이 시각적으로 보여줌  
저장되어있는 시간이 되면 과목에 맞는 링크에 접속하여 화상채팅이 열리게됨  

## a_3.py
자신의 수업 시간표를 시간, 과목을 설정하는 GUI  
자신의 과목의 링크, 과목명을 수정 할 수 있음  
> __class EditInterface__  
>> GUI에 사용되는 버튼, QTableWidget 등등의 GUI 구성, 기능 내표 클라스  

> __class WarningMessage__  
>> 시간표를 설정하지 않았을 때 나오는 경고창  

> __class SendToInfoEdit__  
>> 과목의 시간을 설정해주는 클라스  
>> __sjt_timeInfoData.csv__ 에 저장 및 수정함  

> __class ComboBoxInfoEdit__  
>> 시간표 QTableWidget 에 들어가는 과목을 내포하는 QComboBox 위젯의 정보를 내포하는 클라스  

> __class SjtButtonInfo__  
>> 버튼을 누르면 SjtEditWidget(QDialog) 이 열림  
>> 과목이름을 가지고 있는 왼쪽에 나열되는 버튼  

> __class SjtEditWidget__  
>> 과목의 링크 혹은 과목명을 변경 할 수 있는 클라스  
