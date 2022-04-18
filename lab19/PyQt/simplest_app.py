import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton, QHBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App Works')
window.setGeometry(100, 100, 500, 500)

btn1 = QPushButton('OK')
btn2 = QPushButton('Cancel')
main_layout = QHBoxLayout()
main_layout.addWidget(btn1)
main_layout.addWidget(btn2)
window.setLayout(main_layout)

window.show()

sys.exit(app.exec())


