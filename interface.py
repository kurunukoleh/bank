import requests
import json
from PyQt5.QtWidgets import *

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
        color : #ffffff;
        font-size: 15px;
        min-width: 1px;
        min-height : 1px;
        margin : 1 px;
    }

    QPushButton {
        background-color: #cc0000;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        min-width: 100px;
        min-height: 50px;
        font-size: 15px;
        font-family: none;

    }

    QPushButton:hover {
        background-color: #ff2200;
        color : #ffffff;
        border-radius: 10px ;
        border-color: #111111;
        border-style: none;
        border-width: 10px;
        min-height: 50px;
        min-width: 100px;
        font-size: 15px;
        font-family: none;

    }

    
    QLineEdit {
        background-color: #111111 ;
        color : #ffffff;
        font-size: 15px;
        border-color: #000000;
        border-style: none;
        border-width: 1px;
        border-radius: 5px ;
        min-height: 30px;
    }

    QLineEdit:hover {
        background-color: #151515 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        min-height: 50px;
    }


    QLabel{
        background-color: #000000 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
    }

    QLabel:hover{
        background-color: #000000 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #000000;
        border-style: solid;
        border-width: 3px;
    }

""")

window = QWidget()
window.resize(400 , 300)
mainline = QVBoxLayout()

text1 = QLabel('введіть код валюти')
text2 = QLabel('введіть дату')
text3 = QLabel('')

pole1 = QLineEdit()
pole2 = QLineEdit()

btn = QPushButton('взнати')

mainline.addWidget(text1)
mainline.addWidget(pole1)
mainline.addWidget(text2)
mainline.addWidget(pole2)
mainline.addWidget(btn)
mainline.addWidget(text3)

def know():
    valcode = pole1.text()
    date = pole2.text()
    a = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json')
    if a.status_code == 200:
        data = json.loads(a.text)
        text3.setText(data[0]['txt'] + " "+ str(data[0]['rate']))

btn.clicked.connect(know)

window.setLayout(mainline)
window.show()
app.exec()