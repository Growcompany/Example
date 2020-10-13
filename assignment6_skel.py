import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit,  QDial)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        #이름, 나이, 점수, 양 세팅 UI 1번째 줄
        Name = QLabel('Name:')
        Age = QLabel('Age:')
        Score = QLabel('Score:')

        NameEdit = QLineEdit()
        AgeEdit = QLineEdit()
        ScoreEdit = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addWidget(Name)
        hbox.addWidget(NameEdit)
        hbox.addWidget(Age)
        hbox.addWidget(AgeEdit)
        hbox.addWidget(Score)
        hbox.addWidget(ScoreEdit)

        #Amount랑 Key값 선택 2번째 줄
        Amount = QLabel('Amount:')
        AmountEdit = QLineEdit()

        Key = QLabel('Key:')

        cb = QComboBox(self)
        cb.addItem('Age')
        cb.addItem('Name')
        cb.addItem('Score')

        hbox1 = QHBoxLayout()
        hbox1.addStretch(3)
        hbox1.addWidget(Amount)
        hbox1.addWidget(AmountEdit)
        hbox1.addWidget(Key)
        hbox1.addWidget(cb)

        #관리 버튼 UI 3번쨰줄
        Add_Btn = QPushButton("Add", self)
        Del_Btn = QPushButton("Del", self)
        Find_Btn = QPushButton("Find", self)
        Inc_Btn = QPushButton("Inc", self)
        Show_Btn = QPushButton("Show", self)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(2)
        hbox2.addWidget(Add_Btn)
        hbox2.addWidget(Del_Btn)
        hbox2.addWidget(Find_Btn)
        hbox2.addWidget(Inc_Btn)
        hbox2.addWidget(Show_Btn)

        #Result 창 마지막
        Result = QLabel('Result:')
        ResultText = QTextEdit()

        hbox3 = QHBoxLayout()
        hbox3.addWidget(Result)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(ResultText)

        #각 줄 대로 세팅해주기
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)
        self.setWindowTitle('Assignment6')
        self.show()


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass



if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

