txt_title = "Catatan Pengeluaran"
win_width, win_height = 800, 600
win_x, win_y = 300, 150

txt_first = "Welcome to Mimi"
txt_instruction = "Mimi akan membantu kamu mencatat pengeluaran harian"
txt_next = "Mulai Mencatat"

Daily_budget = 500000

user_data = {
    "item": "",
    "amount": 0,
    "category": ""
}

app_style = """ 
QWidget {
font-size: 16 px;
font-family: Arial, sans-serif;
}
QLabel {
font-size: 16px;
padding: 4px;
}
QLineEdit, QComboBox {
font-size: 16px;
padding: 8px;
min-height: 25px;
}
QPushButton {
font-size: 16px;
font-weight: bold;
padding: 10px 20px;
min-height: 30px;
}
"""