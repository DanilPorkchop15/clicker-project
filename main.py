from PyQt5 import QtWidgets
from interface import Ui_BurgerClicker
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    BurgerClicker = QtWidgets.QMainWindow()
    ui = Ui_BurgerClicker()
    ui.setupUi(BurgerClicker)
    BurgerClicker.show()
    sys.exit(app.exec_())

