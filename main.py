from interface import *
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    BurgerClicker = QtWidgets.QMainWindow()
    ui = Ui_BurgerClicker()
    ui.setupUi(BurgerClicker)
    BurgerClicker.show()
    sys.exit(app.exec_())
