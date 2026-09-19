import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

from instr import txt_title, win_width, win_height, win_x ,win_y, txt_instruction, txt_next, txt_first

class Mainn(QWidget):
    def __init__(self):
     super().__init__()
     self.initUi()
     self.connects()
     self.set_appear()
     self.show()

    def initUi(self):
       self.first_txt = QLabel(txt_first)
       self.instruction = QLabel(txt_instruction)
       self.btn_next = QPushButton(txt_next)
       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.first_txt, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.first_txt, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
       self.setLayout(self.layout_line)

    def next_click(self):
       from second import Second 
       self.hide()
       self.sw = Second()
       self.sw.show()
   
    def connects(self):
       self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


app = QApplication(sys.argv)
mw = Mainn()
sys.exit(app.exec_())