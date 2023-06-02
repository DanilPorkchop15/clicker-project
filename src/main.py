from PyQt5 import QtWidgets
from events import Ui_BurgerClickerEvents
import sys



if __name__ == "__main__":

	# Создание экземпляра класса QApplication, представляющего приложение.
	app = QtWidgets.QApplication(sys.argv)
	# Создание экземпляра класса Ui_BurgerClickerEvents, представляющего главное окно приложения.
	window = Ui_BurgerClickerEvents()
	# Запуск главного цикла обработки событий приложения и завершение программы при его завершении.
	sys.exit(app.exec_())
