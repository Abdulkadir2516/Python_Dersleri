import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()

win.setWindowTitle("PYT1 PyQt5")
win.setGeometry(0,0,300,350)

win.setStyleSheet("background-color: yellow;") 

txt_1 = QtWidgets.QLineEdit(win)
txt_1.setGeometry(25,5,250,40)

btn_9 = QtWidgets.QPushButton(win)
btn_9.setGeometry(25,60,50,50)
btn_9.setText("9")
btn_9.setStyleSheet("background-color: blue;") 


btn_8 = QtWidgets.QPushButton(win)
btn_8.setGeometry(85,60,50,50)
btn_8.setText("8")

btn_7 = QtWidgets.QPushButton(win)
btn_7.setGeometry(145,60,50,50)
btn_7.setText("7")

btn_a = QtWidgets.QPushButton(win)
btn_a.setGeometry(205,60,70,50)
btn_a.setText(" <= ")

btn_6 = QtWidgets.QPushButton(win)
btn_6.setGeometry(25,120,50,50)
btn_6.setText("6")

btn_5 = QtWidgets.QPushButton(win)
btn_5.setGeometry(85,120,50,50)
btn_5.setText("5")

btn_4 = QtWidgets.QPushButton(win)
btn_4.setGeometry(145,120,50,50)
btn_4.setText("4")

btn_b = QtWidgets.QPushButton(win)
btn_b.setGeometry(205,120,70,50)
btn_b.setText(" + ")

btn_3 = QtWidgets.QPushButton(win)
btn_3.setGeometry(25,180,50,50)
btn_3.setText("3")

btn_2 = QtWidgets.QPushButton(win)
btn_2.setGeometry(85,180,50,50)
btn_2.setText("2")

btn_1 = QtWidgets.QPushButton(win)
btn_1.setGeometry(145,180,50,50)
btn_1.setText("1")

btn_c = QtWidgets.QPushButton(win)
btn_c.setGeometry(205,180,70,50)
btn_c.setText(" - ")

btn_0 = QtWidgets.QPushButton(win)
btn_0.setGeometry(25,240,50,50)
btn_0.setText("0")

btn_f = QtWidgets.QPushButton(win)
btn_f.setGeometry(85,240,50,50)
btn_f.setText(" / ")

btn_d = QtWidgets.QPushButton(win)
btn_d.setGeometry(145,240,50,50)
btn_d.setText(" * ")

btn_e = QtWidgets.QPushButton(win)
btn_e.setGeometry(205,240,70,50)
btn_e.setText(" = ")

win.show()
sys.exit(app.exec_()) # bu ifade pencerede çarpı işaretine tıkladığımızda projeyi sonlandırı








"""
lbl_1 = QtWidgets.QLabel(win)
lbl_1.setText("Uygulamamıza Hoş Geldiniz: ")
lbl_1.setGeometry(25,1,200,50)

lbl_2 = QtWidgets.QLabel(win)
lbl_2.setText("Adınız: ")
lbl_2.move(10,52)

txt_1 = QtWidgets.QLineEdit(win)
txt_1.move(60,52)

lbl_3 = QtWidgets.QLabel(win)
lbl_3.setText("Soyadınız: ")
lbl_3.move(10,90)

txt_2 = QtWidgets.QLineEdit(win)
txt_2.move(60,90)

btn_1 = QtWidgets.QPushButton(win)
btn_1.setText("Bana Basma")
btn_1.setGeometry(25,120,100,30)

lbl_4 = QtWidgets.QLabel(win)
lbl_4.setGeometry(25,160,100,30)


def bas():
    sonuc = "İsim => " + txt_1.text() + "  " + txt_2.text()
    print(sonuc)
    lbl_4.setText(sonuc)
    # lbl_4.setMinimumWidth(len(sonuc)) #setMinimumSize(30,len(sonuc))
    # print(int(txt_1.text()) + int(txt_2.text()))


btn_1.clicked.connect(bas)
"""


