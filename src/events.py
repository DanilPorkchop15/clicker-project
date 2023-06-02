from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow
import webbrowser
from random import randint
import time
from PyQt5.QtMultimedia import QSound, QMediaPlayer, QMediaPlaylist, QMediaContent
import statisticsBC
import numpy as np

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

		self.upgrade_count_list = [[],[]]
		self.upgrade_buy_list = [[],[]]
		
		for i in range(0, 6):
			self.upgrade_count_list[0].append(self.stats[8 + i])
			self.upgrade_count_list[1].append(self.stats[14 + i])
			self.upgrade_buy_list[0].append(round(self.stats[20 + i]))
			self.upgrade_buy_list[1].append(round(self.stats[26 + i]))
			
		self.upgrade_count_list = np.array(self.upgrade_count_list)
		self.upgrade_buy_list = np.array(self.upgrade_buy_list)
		
		self.burger_count, self.helps_speed_count, self.click_power, \
			self.allCount, self.allUpgrades, self.allMainUpgrades, self.allHelpUpgrades = self.stats[0:7]
		self.mute = self.stats[32]
		
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
		
		self.player = QMediaPlayer()
		

		self.playlist = QMediaPlaylist()
		media = QMediaContent(QtCore.QUrl.fromLocalFile("sfx/ambience.wav"))
		self.playlist.addMedia(media)
		self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
		self.player.setPlaylist(self.playlist)
		self.player.setVolume(8)
		self.player.play()
		if self.mute:
			self.player.setMuted(True)
		
		self.timer = QtCore.QTimer()
		
		self.events()
		def move_window(event):
			if event.button() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()
				
		self.ui.statisticsFrame.mouseMoveEvent = move_window
		
		self.show()
		
	def events(self):
		self.check_disabled_objects()
		
		self.ui.burgerButton.clicked.connect(lambda: self.onclick())
		self.ui.upgradesButton.clicked.connect(lambda: self.open_main_upgrades())
		self.ui.helpsButton.clicked.connect(lambda: self.open_help_upgrades())
		self.ui.settingsMenuButton.clicked.connect(lambda: self.open_or_close_settings())
		self.ui.muteButton.clicked.connect(lambda: self.mute_or_unmute())
		self.ui.returnButton.clicked.connect(lambda: self.open_or_close_settings())
		self.ui.saveAndExitButton.clicked.connect(lambda: self.save_exit())
		self.ui.telegramButton.clicked.connect(lambda: self.open_social(self.telegram_url))
		self.ui.githubButton.clicked.connect(lambda: self.open_social(self.github_url))
		
		self.timer.timeout.connect(self.auto_click)
		self.timer.start(1000)
		
		self.ui.mainUpgradeBuy.clicked.connect(lambda: self.upgrade(0, 0, self.upgrade_buy_list[0][0],
		                                                            self.upgrade_count_list[0][0],
		                                                            self.ui.mainUpgradeName,
		                                                            self.ui.mainUpgradeBuy,
		                                                            0.2, 'Размер рта'))
		self.ui.mainUpgradeBuy_2.clicked.connect(lambda: self.upgrade(0, 1, self.upgrade_buy_list[0][1],
		                                                              self.upgrade_count_list[0][1],
		                                                              self.ui.mainUpgradeName_2,
		                                                              self.ui.mainUpgradeBuy_2,
		                                                              0.5, 'Мощность челюсти'))
		self.ui.mainUpgradeBuy_3.clicked.connect(lambda: self.upgrade(0, 2, self.upgrade_buy_list[0][2],
		                                                              self.upgrade_count_list[0][2],
		                                                              self.ui.mainUpgradeName_3,
		                                                              self.ui.mainUpgradeBuy_3,
		                                                              1, 'Объем желудка'))
		self.ui.mainUpgradeBuy_4.clicked.connect(lambda: self.upgrade(0, 3, self.upgrade_buy_list[0][3],
		                                                              self.upgrade_count_list[0][3],
		                                                              self.ui.mainUpgradeName_4,
		                                                              self.ui.mainUpgradeBuy_4,
		                                                              3, 'Сила кишки'))
		self.ui.mainUpgradeBuy_5.clicked.connect(lambda: self.upgrade(0, 4, self.upgrade_buy_list[0][4],
		                                                              self.upgrade_count_list[0][4],
		                                                              self.ui.mainUpgradeName_5,
		                                                              self.ui.mainUpgradeBuy_5,
		                                                              10, 'Аппетит'))
		self.ui.mainUpgradeBuy_6.clicked.connect(lambda: self.main_upgrade_6())
		
		self.ui.helpUpgradeBuy.clicked.connect(lambda: self.upgrade(1, 0, self.upgrade_buy_list[1][0],
		                                                              self.upgrade_count_list[1][0],
		                                                              self.ui.helpUpgradeName,
		                                                              self.ui.helpUpgradeBuy,
		                                                              0.5, 'Капризный ребенок'))
		self.ui.helpUpgradeBuy_2.clicked.connect(lambda: self.upgrade(1, 1, self.upgrade_buy_list[1][1],
		                                                              self.upgrade_count_list[1][1],
		                                                              self.ui.helpUpgradeName_2,
		                                                              self.ui.helpUpgradeBuy_2,
		                                                              2, 'Бедный студент'))
		self.ui.helpUpgradeBuy_3.clicked.connect(lambda: self.upgrade(1, 2, self.upgrade_buy_list[1][2],
		                                                              self.upgrade_count_list[1][2],
		                                                              self.ui.helpUpgradeName_3,
		                                                              self.ui.helpUpgradeBuy_3,
		                                                              5, 'Уставший работяга'))
		self.ui.helpUpgradeBuy_4.clicked.connect(lambda: self.upgrade(1, 3, self.upgrade_buy_list[1][3],
		                                                              self.upgrade_count_list[1][3],
		                                                              self.ui.helpUpgradeName_4,
		                                                              self.ui.helpUpgradeBuy_4,
		                                                              15, 'Любитель поесть'))
		self.ui.helpUpgradeBuy_5.clicked.connect(lambda: self.upgrade(1, 4, self.upgrade_buy_list[1][4],
		                                                              self.upgrade_count_list[1][4],
		                                                              self.ui.helpUpgradeName_5,
		                                                              self.ui.helpUpgradeBuy_5,
		                                                              50, 'Голодный толстяк'))
		self.ui.helpUpgradeBuy_6.clicked.connect(lambda: self.upgrade(1, 5, self.upgrade_buy_list[1][5],
		                                                              self.upgrade_count_list[1][5],
		                                                              self.ui.helpUpgradeName_6,
		                                                              self.ui.helpUpgradeBuy_6,
		                                                              250, 'Америкос'))
		
	def mousePressEvent(self, event) :
		self.clickPosition = event.globalPos()
	
	def open_or_close_settings(self):
		if self.ui.settings.width() == 0:
			self.ui.settings.setFixedWidth(1037)
		else:
			self.ui.settings.setFixedWidth(0)
		self.update_stats()
		if not self.mute: self.settings_sound.play()
	
	def mute_or_unmute(self):
		if self.mute:
			self.mute = False
			self.player.setMuted(False)
			self.ui.iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-mute-100.png"))
			self.ui.muteButton.setText("ВЫКЛЮЧИТЬ")
		else:
			self.mute = True
			self.player.setMuted(True)
			self.ui.iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-volume-100.png"))
			self.ui.muteButton.setText("ВКЛЮЧИТЬ")
		self.ui.muteButton.setIcon(self.ui.iconMute)
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
		self.ui.countLabel.setText(f"Съедено: {round(self.burger_count, 1)} бургеров")
		if not self.mute: self.click_sound.play()
		self.shadow_effect.setColor(QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
		self.ui.burgerButton.setGraphicsEffect(self.shadow_effect)
	
	def check_disabled_objects(self):
		main_upgrades = {
			self.upgrade_buy_list[0][0]: self.ui.mainUpgrade,
			self.upgrade_buy_list[0][1]: self.ui.mainUpgrade_2,
			self.upgrade_buy_list[0][2]: self.ui.mainUpgrade_3,
			self.upgrade_buy_list[0][3]: self.ui.mainUpgrade_4,
			self.upgrade_buy_list[0][4]: self.ui.mainUpgrade_5,
			self.upgrade_buy_list[0][5]: self.ui.mainUpgrade_6
		}
		
		help_upgrades = {
			self.upgrade_buy_list[1][0]: self.ui.helpUpgrade,
			self.upgrade_buy_list[1][1]: self.ui.helpUpgrade_2,
			self.upgrade_buy_list[1][2]: self.ui.helpUpgrade_3,
			self.upgrade_buy_list[1][3]: self.ui.helpUpgrade_4,
			self.upgrade_buy_list[1][4]: self.ui.helpUpgrade_5,
			self.upgrade_buy_list[1][5]: self.ui.helpUpgrade_6
		}
		
		for count, upgrade in main_upgrades.items():
			upgrade.setEnabled(self.burger_count >= count)
		
		for count, upgrade in help_upgrades.items():
			upgrade.setEnabled(self.burger_count >= count)
		
		self.max_burger()
	
	def max_burger(self):
		if self.upgrade_count_list[0][5] == 10:
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
	
	def update_stats(self):
		self.gameSessionTime = round((time.time() - self.startTime))
		self.ui.actualCountLabel.setText(f"Актуальное количество съеденных бургеров: {round(self.burger_count, 1)}")
		self.ui.allCountLabel.setText(f"Общее количество съеденных бургеров {round(self.allCount, 1)}")
		self.ui.clickPowerLabel.setText(f"Сила клика: {round(self.click_power, 1)}")
		self.ui.allUpgradesLabel.setText(f"Общее количество улучшений: {self.allUpgrades}")
		self.ui.allMainUpgradesLabel.setText(f"Количество улучшений клика: {self.allMainUpgrades}")
		self.ui.gameSessionTimeLabel.setText(f"Время, проведенное в игре: {self.gameSessionTime} сек.")
		self.ui.allHelpUpgradesLabel.setText(f"Количество улучшений помощников: {self.allHelpUpgrades}")
	
	def upgrade(self, upgrade_type, upgrade_number, buy_amount, count_variable, name_label, buy_label, power, name):
		self.burger_count -= buy_amount
		if upgrade_type == 0:
			self.allUpgrades += 1
			self.allMainUpgrades += 1
			self.click_power += power * self.upgrade_count_list[0][5]
		else:
			self.allUpgrades += 1
			self.allHelpUpgrades += 1
			self.helps_speed_count += power * self.upgrade_count_list[0][5]
		
		if not self.mute: self.upgrade_sound.play()
		
		name_label.setText(f"{name} X {count_variable + 1}")
		buy_label.setText(f'{round(buy_amount * 1.2)} бургеров')
		
		self.upgrade_buy_list[upgrade_type][upgrade_number] *= 1.2
		self.upgrade_count_list[upgrade_type][upgrade_number] += 1
			
		self.update_count()
		self.check_disabled_objects()
	
	def main_upgrade_6(self):
		if self.burger_count >= self.upgrade_buy_list[0][5]:
			self.burger_count -= self.upgrade_buy_list[0][5]
			self.upgrade_buy_list[0][5] *= 1 + self.upgrade_count_list[0][5] / 2.2
			self.allUpgrades += 1
			self.allMainUpgrades += 1
			self.click_power *= 1.5
			self.helps_speed_count *= 1.5
			self.upgrade_count_list[0][5] += 1
			
			if not self.mute: self.upgrade_sound.play()
			
			self.ui.mainUpgradeName_6.setText(f"Уровень бургера (ур. {self.upgrade_count_list[0][5]})")
			self.ui.nameLabel.setText(self.ui.burger_names_list[self.upgrade_count_list[0][5] - 1])
			self.BurgerIcon = QtGui.QIcon()
			self.BurgerIcon.addPixmap(QtGui.QPixmap(f"images/imgs/бургер{self.upgrade_count_list[0][5]}.png"),
			                             )
			
			self.ui.burgerButton.setIconSize(QtCore.QSize(450, 450))
			self.ui.burgerButton.setIcon(self.BurgerIcon)
			self.ui.mainUpgradeBuy_6.setText(f'{round(self.upgrade_buy_list[0][5])} бургеров')
			self.update_count()
			self.max_burger()
			self.check_disabled_objects()
		
	def save_exit(self):
		self.ui.stats = (
			round(self.burger_count, 1), round(self.helps_speed_count, 1), round(self.click_power, 1), round(self.allCount),
			self.allUpgrades, self.allMainUpgrades, self.gameSessionTime, self.allHelpUpgrades,
			self.upgrade_count_list[0][0], self.upgrade_count_list[0][1], self.upgrade_count_list[0][2],
			self.upgrade_count_list[0][3], self.upgrade_count_list[0][4], self.upgrade_count_list[0][5],
			self.upgrade_count_list[1][0], self.upgrade_count_list[1][1], self.upgrade_count_list[1][2],
			self.upgrade_count_list[1][3], self.upgrade_count_list[1][4], self.upgrade_count_list[1][5],
			round(self.upgrade_buy_list[0][0]), round(self.upgrade_buy_list[0][1]), round(self.upgrade_buy_list[0][2]),
			round(self.upgrade_buy_list[0][3]), round(self.upgrade_buy_list[0][4]), round(self.upgrade_buy_list[0][5]),
			round(self.upgrade_buy_list[1][0]), round(self.upgrade_buy_list[1][1]), round(self.upgrade_buy_list[1][2]),
			round(self.upgrade_buy_list[1][3]), round(self.upgrade_buy_list[1][4]), round(self.upgrade_buy_list[1][5]),
			self.mute
		)
		with open('statisticsBC.py', 'w+') as file:
			file.writelines(f'stats = {self.ui.stats}')
		self.close()
	
	def closeEvent(self, event):
		self.timer.stop()
		
	def auto_click(self):
		self.burger_count += self.helps_speed_count
		self.update_count()
		self.check_disabled_objects()
	
