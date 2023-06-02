from PyQt5 import QtWidgets
from events import Ui_BurgerClickerEvents
import sys



if __name__ == "__main__":
	
	app = QtWidgets.QApplication(sys.argv)
	window = Ui_BurgerClickerEvents()
	sys.exit(app.exec_())
