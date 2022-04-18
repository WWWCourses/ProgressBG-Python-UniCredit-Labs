from mainUI import Ui_MainWindow

import sys

from PyQt5.QtWidgets import (
	QApplication, QMainWindow
)


class Window(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.close)



if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec())