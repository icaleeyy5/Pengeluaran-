from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

from instr import txt_title, win_width, win_height, win_x, win_y, Daily_budget, user_data

class Final(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.connects()
        self.set_appear()

    def initUi(self):
        self.lb_title = QLabel("<b>Hasil & Ringkasan Pengeluaran</b>")
        remaining = Daily_budget- user_data["amount"]
        if remaining >=0:
            status = "<fontcolor = 'green' ><b> Aman </b></font>"
        else:
            status = "<fontcolor = 'red' ><b> Woi Over Budget! </b></font>"

        self.lb_item = QLabel(f"Keterangan Pengeluaran:<b>{user_data['item']}</b>")
        self.lb_amount = QLabel(f"Nominal:<b>Rp{user_data['amount']:,}</b>")
        self.lb_category = QLabel(f"Kategori:<b>{user_data['category']}</b>")
        self.lb_status = QLabel(f"Sisa Anggaran:<b>Rp{remaining:,}</b> | Status : {status} ")
        self.btn_close = QPushButton("Tombol tutup disini :D")
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.lb_title, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.lb_item)
        self.layout_line.addWidget(self.lb_amount)
        self.layout_line.addWidget(self.lb_category)
        self.layout_line.addWidget(self.lb_status)
        self.layout_line.addWidget(self.btn_close, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def connects(self):
        self.btn_close.clicked.connect(self.close)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)