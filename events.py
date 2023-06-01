from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
import sys
import webbrowser
import threading
from random import randint
import time
from PyQt5.QtMultimedia import QSound
import statisticsBC

class Ui_BurgerClickerEvents(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.default_stats = (0, 0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
		                      10, 100, 300, 1000, 2500, 200, 100, 500, 1000, 3000, 10000, 25000, False)
		self.stats = statisticsBC.stats
		with open('statisticsBC.py', 'w+') as file:
			file.write(f'stats = {self.default_stats}')
		self.startTime = time.time()
		self.gameSessionTime = self.stats[6]
		
		for i in range(0, 6):
			setattr(self, f"main_count_{i+1}", self.stats[8 + i])
			setattr(self, f"help_count_{i+1}", self.stats[14 + i])
			setattr(self, f"main_buy_{i+1}", round(self.stats[20 + i]))
			setattr(self, f"help_buy_{i+1}", round(self.stats[26 + i]))
		
		self.burger_count, self.helps_speed_count, self.click_power, \
			self.allCount, self.allUpgrades, self.allMainUpgrades, self.allHelpUpgrades = self.stats[0:7]
		self.mute = self.stats[32]
		self.iconMute = QtGui.QIcon()
		
		self.burger_names_list = [
			'Вонючий бургер',
			'Гамбургер',
			'Двойной чизбургер',
			'Воппер',
			'Двойной воппер',
			'Тройной воппер',
			'Элитный бургер',
			'Мегамяс',
			'Королевский бургер',
			'Великий божественный бургер'
		]
		self.BurgerIcon = QtGui.QIcon()
		self.BurgerIcon.addPixmap(QtGui.QPixmap(f":/images/бургер{self.stats[13]}.png"))
		self.telegram_url = 'https://t.me/porkchoppppppp'
		self.github_url = 'https://github.com/DanilPorkchop15'
		self.click_sound = QSound('sfx/click.wav', self)
		self.upgrade_sound = QSound('sfx/upgrade.wav', self)
		self.settings_sound = QSound('sfx/settings.wav', self)
		
		self.shadow_effect = QtWidgets.QGraphicsDropShadowEffect()
		self.shadow_effect.setBlurRadius(70)
		self.shadow_effect.setOffset(0, 10)
		
		self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))
		
		self.ui.centralwidget.setGraphicsEffect(self.shadow)
		
		self.check_disabled_objects()
		
		thread = threading.Thread(target=self.auto_click)
		thread.start()
		
		self.ui.burgerButton.clicked.connect(lambda: self.onclick())
		self.ui.upgradesButton.clicked.connect(lambda: self.open_main_upgrades())
		self.ui.helpsButton.clicked.connect(lambda: self.open_help_upgrades())
		self.ui.settingsMenuButton.clicked.connect(lambda: self.open_or_close_settings())
		self.ui.muteButton.clicked.connect(lambda: self.mute_or_unmute())
		self.ui.returnButton.clicked.connect(lambda: self.open_or_close_settings())
		self.ui.saveAndExitButton.clicked.connect(lambda: self.save_exit())
		self.ui.telegramButton.clicked.connect(lambda: self.open_social(self.telegram_url))
		self.ui.githubButton.clicked.connect(lambda: self.open_social(self.github_url))
		
		self.ui.mainUpgradeBuy.clicked.connect(lambda: self.main_upgrade_1())
		self.ui.mainUpgradeBuy_2.clicked.connect(lambda: self.main_upgrade_2())
		self.ui.mainUpgradeBuy_3.clicked.connect(lambda: self.main_upgrade_3())
		self.ui.mainUpgradeBuy_4.clicked.connect(lambda: self.main_upgrade_4())
		self.ui.mainUpgradeBuy_5.clicked.connect(lambda: self.main_upgrade_5())
		self.ui.mainUpgradeBuy_6.clicked.connect(lambda: self.main_upgrade_6())
		
		self.ui.helpUpgradeBuy.clicked.connect(lambda: self.help_upgrade_1())
		self.ui.helpUpgradeBuy_2.clicked.connect(lambda: self.help_upgrade_2())
		self.ui.helpUpgradeBuy_3.clicked.connect(lambda: self.help_upgrade_3())
		self.ui.helpUpgradeBuy_4.clicked.connect(lambda: self.help_upgrade_4())
		self.ui.helpUpgradeBuy_5.clicked.connect(lambda: self.help_upgrade_5())
		self.ui.helpUpgradeBuy_6.clicked.connect(lambda: self.help_upgrade_6())
		
		self.show()
	def open_or_close_settings(self):
		if self.ui.settings.width() == 0:
			self.ui.settings.setFixedWidth(1037)
		else:
			self.ui.settings.setFixedWidth(0)
		self.updade_stats()
		if not self.mute: self.settings_sound.play()
	
	def mute_or_unmute(self):
		if self.mute:
			self.mute = False
			self.iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-mute-100.png"))
			self.ui.muteButton.setText("Выключить")
		else:
			self.mute = True
			self.iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-volume-100.png"))
			self.ui.muteButton.setText("Включить")
		self.ui.muteButton.setIcon(self.iconMute)
		if not self.mute: self.settings_sound.play()
	
	def open_social(self, url):
		webbrowser.open_new_tab(url)
		if not self.mute: self.settings_sound.play()
	
	def update_count(self):
		self.ui.countLabel.setText(f"Съедено: {round(self.burger_count, 1)} бургеров")
		self.ui.helpCountLabel.setText(f"Помощь: {round(self.helps_speed_count, 1)}/сек")
	
	def onclick(self):
		self.burger_count += self.click_power
		self.allCount += self.click_power
		self.check_disabled_objects()
		self.update_count()
		if not self.mute: self.click_sound.play()
		self.shadow_effect.setColor(QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
		self.ui.burgerButton.setGraphicsEffect(self.shadow_effect)
	
	def check_disabled_objects(self):
		main_upgrades = {
			self.main_buy_1: self.ui.mainUpgrade,
			self.main_buy_2: self.ui.mainUpgrade_2,
			self.main_buy_3: self.ui.mainUpgrade_3,
			self.main_buy_4: self.ui.mainUpgrade_4,
			self.main_buy_5: self.ui.mainUpgrade_5,
			self.main_buy_6: self.ui.mainUpgrade_6
		}
		
		help_upgrades = {
			self.help_buy_1: self.ui.helpUpgrade,
			self.help_buy_2: self.ui.helpUpgrade_2,
			self.help_buy_3: self.ui.helpUpgrade_3,
			self.help_buy_4: self.ui.helpUpgrade_4,
			self.help_buy_5: self.ui.helpUpgrade_5,
			self.help_buy_6: self.ui.helpUpgrade_6
		}
		
		for count, upgrade in main_upgrades.items():
			upgrade.setEnabled(self.burger_count >= count)
		
		for count, upgrade in help_upgrades.items():
			upgrade.setEnabled(self.burger_count >= count)
		
		self.max_burger()
	
	def max_burger(self):
		if self.main_count_6 == 10:
			self.ui.mainUpgrade_6.setEnabled(False)
			self.ui.mainUpgradeBuy_6.setEnabled(False)
			self.ui.mainUpgradeName_6.setText(f"Уровень бургера (MAX)")
			self.ui.mainUpgradeBuy_6.setText('^_____^')
	
	def open_main_upgrades(self):
		if self.ui.mainUpgradeFrame.width() == 0:
			self.ui.mainUpgradeFrame.setMaximumWidth(21312312)
			self.ui.helpUpgradeFrame.setMaximumWidth(0)
		if not self.mute: self.settings_sound.play()
	
	def open_help_upgrades(self):
		if self.ui.helpUpgradeFrame.width() == 0:
			self.ui.helpUpgradeFrame.setMaximumWidth(21312312)
			self.ui.mainUpgradeFrame.setMaximumWidth(0)
		if not self.mute: self.settings_sound.play()
	
	def updade_stats(self):
		self.gameSessionTime = round((time.time() - self.startTime))
		self.ui.actualCountLabel.setText(f"Актуальное количество съеденных бургеров: {round(self.burger_count, 1)}")
		self.ui.allCountLabel.setText(f"Общее количество съеденных бургеров {round(self.allCount, 1)}")
		self.ui.clickPowerLabel.setText(f"Сила клика: {round(self.click_power, 1)}")
		self.ui.allUpgradesLabel.setText(f"Общее количество улучшений: {self.allUpgrades}")
		self.ui.allMainUpgradesLabel.setText(f"Количество улучшений клика: {self.allMainUpgrades}")
		self.ui.gameSessionTimeLabel.setText(f"Время, проведенное в игре: {self.gameSessionTime} сек.")
		self.ui.allHelpUpgradesLabel.setText(f"Количество улучшений помощников: {self.allHelpUpgrades}")
	
	def main_upgrade(self, buy_amount, count_variable, name_label, buy_label, power, name):
		self.burger_count -= buy_amount
		self.allUpgrades += 1
		self.allMainUpgrades += 1
		self.click_power += power * self.main_count_6
		
		if not self.mute: self.upgrade_sound.play()
		
		name_label.setText(f"{name} X {count_variable + 1}")
		buy_label.setText(f'{round(buy_amount * 1.2)} бургеров')
		
		self.update_count()
	
	def main_upgrade_1(self):
		self.main_upgrade(self.main_buy_1, self.main_count_1, self.ui.mainUpgradeName,
						  self.ui.mainUpgradeBuy, 0.2, 'Размер рта')
		self.main_buy_1 *= 1.2
		self.main_count_1 += 1
		self.check_disabled_objects()
	
	def main_upgrade_2(self):
		self.main_upgrade(self.main_buy_2, self.main_count_2, self.ui.mainUpgradeName_2,
			    		  self.ui.mainUpgradeBuy_2, 0.5, 'Мощность челюсти')
		self.main_buy_2 *= 1.2
		self.main_count_2 += 1
		self.check_disabled_objects()
	
	def main_upgrade_3(self):
		self.main_upgrade(self.main_buy_3, self.main_count_3, self.ui.mainUpgradeName_3,
						  self.ui.mainUpgradeBuy_3, 1, 'Объем желудка')
		self.main_buy_3 *= 1.2
		self.main_count_3 += 1
		self.check_disabled_objects()
	
	def main_upgrade_4(self):
		self.main_upgrade(self.main_buy_4, self.main_count_4, self.ui.mainUpgradeName_4,
						  self.ui.mainUpgradeBuy_4, 3, 'Сила кишки')
		self.main_buy_4 *= 1.2
		self.main_count_4 += 1
		self.check_disabled_objects()
	
	def main_upgrade_5(self):
		self.main_upgrade(self.main_buy_5, self.main_count_5, self.ui.mainUpgradeName_5,
						  self.ui.mainUpgradeBuy_5, 10, 'Аппетит')
		self.main_buy_5 *= 1.2
		self.main_count_5 += 1
		self.check_disabled_objects()
	
	def main_upgrade_6(self):
		if self.burger_count >= self.main_buy_6:
			self.burger_count -= self.main_buy_6
			self.main_buy_6 *= 1 + self.main_count_6 / 2.2
			self.allUpgrades += 1
			self.allMainUpgrades += 1
			self.click_power *= 1.5
			self.helps_speed_count *= 1.5
			self.main_count_6 += 1
			
			if not self.mute: self.upgrade_sound.play()
			
			self.ui.mainUpgradeName_6.setText(f"Уровень бургера (ур. {self.main_count_6})")
			self.ui.nameLabel.setText(self.burger_names_list[self.main_count_6 - 1])
			self.BurgerIcon = QtGui.QIcon()
			self.BurgerIcon.addPixmap(QtGui.QPixmap(f"images/imgs/бургер{self.main_count_6}.png"),
			                             )
			
			self.ui.burgerButton.setIconSize(QtCore.QSize(450, 450))
			self.ui.burgerButton.setIcon(self.BurgerIcon)
			self.ui.mainUpgradeBuy_6.setText(f'{round(self.main_buy_6)} бургеров')
			self.update_count()
			self.max_burger()
			self.check_disabled_objects()
	
	def help_upgrade(self, buy_amount, count_variable, name_label, buy_label, power, name):
		if self.burger_count >= buy_amount:
			
			self.burger_count -= buy_amount
			self.allUpgrades += 1
			self.allHelpUpgrades += 1
			self.helps_speed_count += power * self.main_count_6
			
			if not self.mute: self.upgrade_sound.play()
			
			name_label.setText(f"{name} X {count_variable + 1}")
			buy_label.setText(f'{round(buy_amount * 1.2)} бургеров')
			
			self.update_count()
	
	def help_upgrade_1(self):
		self.help_upgrade(self.help_buy_1, self.help_count_1, self.ui.helpUpgradeName,
						  self.ui.helpUpgradeBuy, 0.5, 'Капризный ребенок')
		self.help_buy_1 *= 1.2
		self.help_count_1 += 1
		self.check_disabled_objects()
	
	def help_upgrade_2(self):
		self.help_upgrade(self.help_buy_2, self.help_count_2, self.ui.helpUpgradeName_2,
						  self.ui.helpUpgradeBuy_2, 2, 'Бедный студент')
		self.help_buy_2 *= 1.2
		self.help_count_2 += 1
		self.check_disabled_objects()
	
	def help_upgrade_3(self):
		self.help_upgrade(self.help_buy_3, self.help_count_3, self.ui.helpUpgradeName_3,
						  self.ui.helpUpgradeBuy_3, 5, 'Уставший работяга')
		self.help_buy_3 *= 1.2
		self.help_count_3 += 1
		self.check_disabled_objects()
	
	def help_upgrade_4(self):
		self.help_upgrade(self.help_buy_4, self.help_count_4, self.ui.helpUpgradeName_4,
						  self.ui.helpUpgradeBuy_4, 15, 'Любитель поесть')
		self.help_buy_4 *= 1.2
		self.help_count_4 += 1
		self.check_disabled_objects()
	
	def help_upgrade_5(self):
		self.help_upgrade(self.help_buy_5, self.help_count_5, self.ui.helpUpgradeName_5,
						  self.ui.helpUpgradeBuy_5, 50, 'Голодный толстяк')
		self.help_buy_5 *= 1.2
		self.help_count_5 += 1
		self.check_disabled_objects()
	
	def help_upgrade_6(self):
		self.help_upgrade(self.help_buy_6, self.help_count_6, self.ui.helpUpgradeName_6,
						  self.ui.helpUpgradeBuy_6, 250, 'Америкос')
		self.help_buy_6 *= 1.2
		self.help_count_6 += 1
		self.check_disabled_objects()
		
		
	def save_exit(self):
		self.ui.stats = (round(self.burger_count), round(self.helps_speed_count), round(self.click_power, 1),
		              round(self.allCount),self.allUpgrades, self.allMainUpgrades, self.gameSessionTime,
		              self.allHelpUpgrades,
					  self.main_count_1, self.main_count_2, self.main_count_3, self.main_count_4,
					  self.main_count_5, self.main_count_6, self.help_count_1, self.help_count_2,
					  self.help_count_3, self.help_count_4, self.help_count_5, self.help_count_6,
					  round(self.main_buy_1), round(self.main_buy_2), round(self.main_buy_3), round(self.main_buy_4),
					  round(self.main_buy_5),round(self.main_buy_6), round(self.help_buy_1),
					  round(self.help_buy_2), round(self.help_buy_3), round(self.help_buy_4),
					  round(self.help_buy_5), round(self.help_buy_6), self.mute)
		with open('statisticsBC.py', 'w+') as file:
			file.writelines(f'stats = {self.ui.stats}')
		self.close()
		
	def auto_click(self):
		self.burger_count += self.helps_speed_count
		self.update_count()
		threading.Timer(1.0, self.auto_click).start()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Ui_BurgerClickerEvents()
	sys.exit(app.exec_())
