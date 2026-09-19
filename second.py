from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QMessageBox)

from instr import txt_title, win_width, win_height, win_x, win_y, user_data

class Second(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.connects()
        self.set_appear()

    def initUi(self):
        self.lb_title = QLabel("<b>Form Input Pengeluaran</b>")
        self.input_item = QLineEdit()
        self.input_item.setPlaceholderText("Keterangan Pengeluaran:")
        self.input_amount = QLineEdit()
        self.input_amount.setPlaceholderText("Nominal Pengeluaran (Rp)")
        self.combo_category = QComboBox()
        self.combo_category.addItems(["Makanan & Minuman", "Transportasi", "Kebutuhan Belajar", "Hiburan", "Kebutuhan"])
        self.btn_next = QPushButton("Proses & Lihat Hasil")
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.input_item)
        self.layout_line.addWidget(self.input_amount)
        self.layout_line.addWidget(self.combo_category)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        item = self.input_item.text().strip()
        amount_text = self.input_amount.text().strip()
        if not item or not amount_text:
            QMessageBox.warning(self, "Peringatan", "Semua kolom input harus diisi!")
            return
        try:
            amount = int(amount_text)
        except ValueError:
            QMessageBox.warning(self, "Input Salah", "Nominal pengeluaran harus berupa angka!")
            return
        user_data["item"] = item
        user_data["amount"] = amount
        user_data["category"] = self.combo_category.currentText()
        from final import Final
        self.hide()
        self.fw = Final()
        self.fw.show()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)



