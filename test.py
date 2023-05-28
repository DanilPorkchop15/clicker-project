from interface import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_BurgerClicker()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())