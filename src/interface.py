# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets
from images.icons_rc import *
import statisticsBC
import ctypes

myappid = 'PorkchopInc.Burger_Clicker.Burger_Clicker.v1.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Ui_MainWindow(QtWidgets.QMainWindow):
	def setupUi(self, BurgerClicker):
		self.stats = statisticsBC.stats

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

		self.iconMute = QtGui.QIcon()
		
		self.BurgerIcon.addPixmap(QtGui.QPixmap(f"images/imga/бургер{self.stats[13]}.png"), QtGui.QIcon.Normal,
		                          QtGui.QIcon.Off)
		self.shadow_effect = QtWidgets.QGraphicsDropShadowEffect()
		self.shadow_effect.setBlurRadius(70)
		self.shadow_effect.setOffset(0, 10)
		
		BurgerClicker.setWindowIcon(QtGui.QIcon('images/icons/free-icon-burger-5787014.png'))
		BurgerClicker.resize(1037, 780)
		BurgerClicker.setMinimumSize(QtCore.QSize(1037, 780))
		BurgerClicker.setMaximumSize(QtCore.QSize(1037, 780))
		BurgerClicker.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		BurgerClicker.setObjectName("BurgerClicker")
		BurgerClicker.setStyleSheet("QWidget{\n"
		                            "    background-color: #b1f0cc;\n"
		                            "}\n"
		                            "\n"
		                            "*{\n"
		                            "    font-size: 12px;\n"
		                            "    font-family: \"Verdana\";\n"
		                            "}\n"
		                            "\n"
		                            "QPushButton:pressed{\n"
		                            "    background-color:rgba(255, 255, 255, 0);\n"
		                            "}\n"
		                            "\n"
		                            "#clickerFrame{\n"
		                            "    background-color: rgba(255, 255, 255, 0.5);\n"
		                            "    border-radius: 30px;\n"
		                            "}\n"
		                            "\n"
		                            "#clickerFrame Qlaber{\n"
		                            "    background-color: rgba(255, 255, 255, 0.3);\n"
		                            "}\n"
		                            "\n"
		                            "#burgerButton{\n"
		                            "    background-color:rgba(255, 255, 255, 0);\n"
		                            "}\n"
		                            "\n"
		                            "#mainUpgradeFrame QFrame{\n"
		                            "        background-color: #8edeb0;\n"
		                            "        border-radius: 22px;\n"
		                            "}\n"
		                            "\n"
		                            "\n"
		                            "#mainUpgradeFrame QLabel{\n"
		                            "    background-color: none;\n"
		                            "}\n"
		                            "\n"
		                            "#mainUpgradeBuy, #mainUpgradeBuy_2, #mainUpgradeBuy_3, #mainUpgradeBuy_4, #mainUpgradeBuy_5, #mainUpgradeBuy_6 {\n"
		                            "        background-color: rgba(0, 0, 0, 0.05);\n"
		                            "        border-radius: 15px;\n"
		                            "}\n"
		                            "\n"
		                            "#mainUpgradeBuy:hover, #mainUpgradeBuy_2:hover, #mainUpgradeBuy_3:hover, #mainUpgradeBuy_4:hover, #mainUpgradeBuy_5:hover, #mainUpgradeBuy_6:hover{\n"
		                            "        background-color: rgba(142, 123, 123, 0.1);\n"
		                            "        border: 1px solid gray\n"
		                            "}\n"
		                            "\n"
		                            "#mainUpgradeBuy:pressed, #mainUpgradeBuy_2:pressed, #mainUpgradeBuy_3:pressed, #mainUpgradeBuy_4:pressed, #mainUpgradeBuy_5:pressed, #mainUpgradeBuy_6:pressed {\n"
		                            "        background-color: rgba(100, 110, 120, 0.3);\n"
		                            "        transform: scale(0.9);\n"
		                            "}\n"
		                            "\n"
		                            "#helpUpgradeFrame QFrame{\n"
		                            "        background-color: #8edeb0;\n"
		                            "        border-radius: 22px;\n"
		                            "}\n"
		                            "\n"
		                            "\n"
		                            "#helpUpgradeFrame QLabel{\n"
		                            "    background-color: none;\n"
		                            "}\n"
		                            "\n"
		                            "#helpUpgradeBuy, #helpUpgradeBuy_2, #helpUpgradeBuy_3, #helpUpgradeBuy_4, #helpUpgradeBuy_5, #helpUpgradeBuy_6 {\n"
		                            "        background-color: rgba(0, 0, 0, 0.05);\n"
		                            "        border-radius: 15px;\n"
		                            "}\n"
		                            "\n"
		                            "#helpUpgradeBuy:hover, #helpUpgradeBuy_2:hover, #helpUpgradeBuy_3:hover, #helpUpgradeBuy_4:hover, #helpUpgradeBuy_5:hover, #helpUpgradeBuy_6:hover{\n"
		                            "        background-color: rgba(142, 123, 123, 0.1);\n"
		                            "        border: 1px solid gray\n"
		                            "}\n"
		                            "\n"
		                            "#helpUpgradeBuy:pressed, #helpUpgradeBuy_2:pressed, #helpUpgradeBuy_3:pressed, #helpUpgradeBuy_4:pressed, #helpUpgradeBuy_5:pressed, #helpUpgradeBuy_6:pressed {\n"
		                            "        background-color: rgba(100, 110, 120, 0.3);\n"
		                            "        transform: scale(0.9);\n"
		                            "}\n"
		                            "\n"
		                            "#upgradeFrame{\n"
		                            "    background-color: rgba(0, 0, 0, 0.12);\n"
		                            "    border-radius: 27px;\n"
		                            "}\n"
		                            "\n"
		                            "#mainUpgradeFrame, #helpUpgradeFrame{\n"
		                            "    background-color: #b1f0cc;\n"
		                            "    border-radius: 25px;\n"
		                            "}\n"
		                            "\n"
		                            "#mainUpgradeMenuFrame{\n"
		                            "    background-color: rgba(0, 0, 0, 0)\n"
		                            "}\n"
		                            "\n"
		                            "#selectUpgradeFrame{\n"
		                            "    background-color:rgba(255, 255, 255, 0);\n"
		                            "}\n"
		                            "#upgradesButton{\n"
		                            "    border-top-left-radius: 20px;\n"
		                            "    border-bottom-left-radius: 20px\n"
		                            "}\n"
		                            "\n"
		                            "#helpsButton{\n"
		                            "    border-top-right-radius: 20px;\n"
		                            "    border-bottom-right-radius: 20px\n"
		                            "}\n"
		                            "\n"
		                            "#helpsButton:hover, #upgradesButton:hover{\n"
		                            "        background-color: rgba(0, 0, 0, 0.1);\n"
		                            "}\n"
		                            "\n"
		                            "\n"
		                            "#helpsButton:pressed, #upgradesButton:pressed{\n"
		                            "        background-color: rgba(0, 50, 0, 0.2);\n"
		                            "}\n"
		                            "\n"
		                            "#nameLabel {\n"
		                            "    border-radius: 19px\n"
		                            "}\n"
		                            "\n"
		                            "#countLabel{\n"
		                            "    border-radius: 20px;\n"
		                            "    background-color: #b1f0cc\n"
		                            "}\n"
		                            "\n"
		                            "#helpCountLabel{\n"
		                            "    border-radius: 15px;\n"
		                            "    background-color: #b1f0cc\n"
		                            "}\n"
		                            "#statisticsFrame{\n"
		                            "    border-radius: 30px;\n"
		                            "    background-color: rgba(0, 0, 0, 0.12)\n"
		                            "}\n"
		                            "\n"
		                            "#settingsFrame QPushButton{\n"
		                            "    border-radius: 25px;\n"
		                            "    \n"
		                            "    background-color: rgba(0, 0, 0, 0.12);\n"
		                            "}\n"
		                            "\n"
		                            "#settingsFrame QPushButton:hover{\n"
		                            "        background-color: rgba(0, 0, 0, 0.18);\n"
		                            "}\n"
		                            "\n"
		                            "#settingsFrame QPushButton:pressed{\n"
		                            "        background-color: rgba(0, 0, 0, 0.3);\n"
		                            "}\n"
		                            "\n"
		                            "#githubFrame QPushButton{\n"
		                            "    border-radius: 25px;\n"
		                            "    \n"
		                            "    background-color: rgba(0, 0, 0, 0.12);\n"
		                            "}\n"
		                            "\n"
		                            "#githubFrame QPushButton:hover{\n"
		                            "        background-color: rgba(0, 0, 0, 0.18);\n"
		                            "}\n"
		                            "\n"
		                            "#githubFrame QPushButton:pressed{\n"
		                            "        background-color: rgba(0, 0, 0, 0.3);\n"
		                            "}\n"
		                            "\n"
		                            "#telegramFrame QPushButton{\n"
		                            "    border-radius: 25px;\n"
		                            "    \n"
		                            "    background-color: rgba(0, 0, 0, 0.12);\n"
		                            "}\n"
		                            "\n"
		                            "#telegramFrame QPushButton:hover{\n"
		                            "        background-color: rgba(0, 0, 0, 0.18);\n"
		                            "}\n"
		                            "\n"
		                            "#telegramFrame QPushButton:pressed{\n"
		                            "        background-color: rgba(0, 0, 0, 0.3);\n"
		                            "}\n"
		                            "\n"
		                            "\n"
		                            "#settings{\n"
		                            "    background-color: rgba(21, 55, 12, 0.3);\n"
		                            "}\n"
		                            "\n"
		                            "#settingsWrapper{\n"
		                            "    border-radius: 50px;\n"
		                            "}\n"
		                            "\n"
		                            "#settings QPushButton{\n"
		                            "    border-radius: 20px;\n"
		                            "    background-color: rgba(255, 255, 255, 0.4)\n"
		                            "}\n"
		                            "\n"
		                            "#settings QPushButton:hover{\n"
		                            "        background-color: rgba(142, 123, 123, 0.1);\n"
		                            "        border: 1px solid gray\n"
		                            "}\n"
		                            "\n"
		                            "#settings QPushButton:pressed{\n"
		                            "        background-color: rgba(0, 0, 0, 0.2);\n"
		                            "}\n"
		                            "\n"
		                            "#statisticsToolBox QWidget{\n"
		                            "    border-radius: 20px;\n"
		                            "}\n"
		                            "\n"
		                            "#statisticsToolBox QLabel{\n"
		                            "    border-radius: 5px;\n"
		                            "    background-color: rgba(255, 255, 255, 0.4)\n"
		                            "}\n"
		                            "\n"
		                            "#statisticsToolBox QLine{\n"
		                            "    background-color: rgba(0, 0, 0, 1)\n"
		                            "}\n"
		                            "")
		self.centralwidget = QtWidgets.QWidget(BurgerClicker)
		self.centralwidget.setEnabled(True)
		self.centralwidget.setAutoFillBackground(False)
		self.centralwidget.setObjectName("centralwidget")
		self.upgradeFrame = QtWidgets.QFrame(self.centralwidget)
		self.upgradeFrame.setGeometry(QtCore.QRect(600, 10, 431, 761))
		self.upgradeFrame.setMinimumSize(QtCore.QSize(431, 761))
		self.upgradeFrame.setMaximumSize(QtCore.QSize(431, 761))
		self.upgradeFrame.setFrameShape(QtWidgets.QFrame.Box)
		self.upgradeFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.upgradeFrame.setLineWidth(1)
		self.upgradeFrame.setMidLineWidth(1)
		self.upgradeFrame.setObjectName("upgradeFrame")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.upgradeFrame)
		self.verticalLayout.setObjectName("verticalLayout")
		self.selectUpgradeFrame = QtWidgets.QFrame(self.upgradeFrame)
		self.selectUpgradeFrame.setMinimumSize(QtCore.QSize(0, 40))
		self.selectUpgradeFrame.setMaximumSize(QtCore.QSize(16777215, 40))
		self.selectUpgradeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.selectUpgradeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.selectUpgradeFrame.setObjectName("selectUpgradeFrame")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.selectUpgradeFrame)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.upgradesButton = QtWidgets.QPushButton(self.selectUpgradeFrame)
		self.upgradesButton.setMinimumSize(QtCore.QSize(0, 40))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.upgradesButton.setFont(font)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons8-купить-обновление-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.upgradesButton.setIcon(icon)
		self.upgradesButton.setIconSize(QtCore.QSize(25, 25))
		self.upgradesButton.setFlat(False)
		self.upgradesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.upgradesButton.setObjectName("upgradesButton")
		self.horizontalLayout.addWidget(self.upgradesButton)
		self.helpsButton = QtWidgets.QPushButton(self.selectUpgradeFrame)
		self.helpsButton.setMinimumSize(QtCore.QSize(0, 40))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.helpsButton.setFont(font)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/icons/icons8-связь-и-помощь-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.helpsButton.setIcon(icon1)
		self.helpsButton.setIconSize(QtCore.QSize(25, 25))
		self.helpsButton.setFlat(False)
		self.helpsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpsButton.setObjectName("helpsButton")
		self.horizontalLayout.addWidget(self.helpsButton)
		self.verticalLayout.addWidget(self.selectUpgradeFrame, 0, QtCore.Qt.AlignTop)
		self.mainUpgradeMenuFrame = QtWidgets.QFrame(self.upgradeFrame)
		self.mainUpgradeMenuFrame.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.mainUpgradeMenuFrame.sizePolicy().hasHeightForWidth())
		self.mainUpgradeMenuFrame.setSizePolicy(sizePolicy)
		self.mainUpgradeMenuFrame.setMaximumSize(QtCore.QSize(1212121, 16777215))
		self.mainUpgradeMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgradeMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgradeMenuFrame.setObjectName("mainUpgradeMenuFrame")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainUpgradeMenuFrame)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setSpacing(0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.mainUpgradeFrame = QtWidgets.QFrame(self.mainUpgradeMenuFrame)
		self.mainUpgradeFrame.setMaximumSize(QtCore.QSize(1234286, 16777215))
		self.mainUpgradeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgradeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgradeFrame.setObjectName("mainUpgradeFrame")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainUpgradeFrame)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.mainUpgrade = QtWidgets.QFrame(self.mainUpgradeFrame)
		self.mainUpgrade.setEnabled(False)
		self.mainUpgrade.setMinimumSize(QtCore.QSize(0, 100))
		self.mainUpgrade.setMaximumSize(QtCore.QSize(16777215, 100))
		self.mainUpgrade.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgrade.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgrade.setObjectName("mainUpgrade")
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.mainUpgrade)
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.mainUpgradeIcon = QtWidgets.QPushButton(self.mainUpgrade)
		self.mainUpgradeIcon.setMinimumSize(QtCore.QSize(50, 0))
		self.mainUpgradeIcon.setMaximumSize(QtCore.QSize(50, 16777215))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/icons/icons8-mouth-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.mainUpgradeIcon.setIcon(icon2)
		self.mainUpgradeIcon.setIconSize(QtCore.QSize(40, 40))
		self.mainUpgradeIcon.setAutoDefault(False)
		self.mainUpgradeIcon.setFlat(True)
		self.mainUpgradeIcon.setObjectName("mainUpgradeIcon")
		self.horizontalLayout_5.addWidget(self.mainUpgradeIcon)
		self.mainUpgradeName = QtWidgets.QLabel(self.mainUpgrade)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.mainUpgradeName.setFont(font)
		self.mainUpgradeName.setObjectName("mainUpgradeName")
		self.horizontalLayout_5.addWidget(self.mainUpgradeName)
		self.mainUpgradeBuy = QtWidgets.QPushButton(self.mainUpgrade)
		self.mainUpgradeBuy.setMinimumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy.setMaximumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(":/icons/icons8-buy-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.mainUpgradeBuy.setIcon(icon3)
		self.mainUpgradeBuy.setObjectName("mainUpgradeBuy")
		self.horizontalLayout_5.addWidget(self.mainUpgradeBuy)
		self.verticalLayout_4.addWidget(self.mainUpgrade)
		self.mainUpgrade_2 = QtWidgets.QFrame(self.mainUpgradeFrame)
		self.mainUpgrade_2.setEnabled(False)
		self.mainUpgrade_2.setMinimumSize(QtCore.QSize(0, 100))
		self.mainUpgrade_2.setMaximumSize(QtCore.QSize(16777215, 100))
		self.mainUpgrade_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgrade_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgrade_2.setObjectName("mainUpgrade_2")
		self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainUpgrade_2)
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.mainUpgradeIcon_2 = QtWidgets.QPushButton(self.mainUpgrade_2)
		self.mainUpgradeIcon_2.setMinimumSize(QtCore.QSize(50, 0))
		self.mainUpgradeIcon_2.setMaximumSize(QtCore.QSize(50, 16777215))
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(":/icons/icons8-denture-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.mainUpgradeIcon_2.setIcon(icon4)
		self.mainUpgradeIcon_2.setIconSize(QtCore.QSize(40, 40))
		self.mainUpgradeIcon_2.setFlat(True)
		self.mainUpgradeIcon_2.setObjectName("mainUpgradeIcon_2")
		self.horizontalLayout_8.addWidget(self.mainUpgradeIcon_2)
		self.mainUpgradeName_2 = QtWidgets.QLabel(self.mainUpgrade_2)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.mainUpgradeName_2.setFont(font)
		self.mainUpgradeName_2.setObjectName("mainUpgradeName_2")
		self.horizontalLayout_8.addWidget(self.mainUpgradeName_2)
		self.mainUpgradeBuy_2 = QtWidgets.QPushButton(self.mainUpgrade_2)
		self.mainUpgradeBuy_2.setMinimumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_2.setMaximumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.mainUpgradeBuy_2.setIcon(icon3)
		self.mainUpgradeBuy_2.setObjectName("mainUpgradeBuy_2")
		self.horizontalLayout_8.addWidget(self.mainUpgradeBuy_2)
		self.verticalLayout_4.addWidget(self.mainUpgrade_2)
		self.mainUpgrade_3 = QtWidgets.QFrame(self.mainUpgradeFrame)
		self.mainUpgrade_3.setEnabled(False)
		self.mainUpgrade_3.setMinimumSize(QtCore.QSize(0, 100))
		self.mainUpgrade_3.setMaximumSize(QtCore.QSize(16777215, 100))
		self.mainUpgrade_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgrade_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgrade_3.setObjectName("mainUpgrade_3")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mainUpgrade_3)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.mainUpgradeIcon_3 = QtWidgets.QPushButton(self.mainUpgrade_3)
		self.mainUpgradeIcon_3.setMinimumSize(QtCore.QSize(50, 0))
		self.mainUpgradeIcon_3.setMaximumSize(QtCore.QSize(50, 16777215))
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(":/icons/icons8-stomach-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.mainUpgradeIcon_3.setIcon(icon5)
		self.mainUpgradeIcon_3.setIconSize(QtCore.QSize(40, 40))
		self.mainUpgradeIcon_3.setFlat(True)
		self.mainUpgradeIcon_3.setObjectName("mainUpgradeIcon_3")
		self.horizontalLayout_4.addWidget(self.mainUpgradeIcon_3)
		self.mainUpgradeName_3 = QtWidgets.QLabel(self.mainUpgrade_3)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.mainUpgradeName_3.setFont(font)
		self.mainUpgradeName_3.setObjectName("mainUpgradeName_3")
		self.horizontalLayout_4.addWidget(self.mainUpgradeName_3)
		self.mainUpgradeBuy_3 = QtWidgets.QPushButton(self.mainUpgrade_3)
		self.mainUpgradeBuy_3.setMinimumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_3.setMaximumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.mainUpgradeBuy_3.setIcon(icon3)
		self.mainUpgradeBuy_3.setObjectName("mainUpgradeBuy_3")
		self.horizontalLayout_4.addWidget(self.mainUpgradeBuy_3)
		self.verticalLayout_4.addWidget(self.mainUpgrade_3)
		self.mainUpgrade_4 = QtWidgets.QFrame(self.mainUpgradeFrame)
		self.mainUpgrade_4.setEnabled(False)
		self.mainUpgrade_4.setMinimumSize(QtCore.QSize(0, 100))
		self.mainUpgrade_4.setMaximumSize(QtCore.QSize(16777215, 100))
		self.mainUpgrade_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgrade_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgrade_4.setObjectName("mainUpgrade_4")
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.mainUpgrade_4)
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.mainUpgradeIcon_4 = QtWidgets.QPushButton(self.mainUpgrade_4)
		self.mainUpgradeIcon_4.setMinimumSize(QtCore.QSize(50, 0))
		self.mainUpgradeIcon_4.setMaximumSize(QtCore.QSize(50, 16777215))
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(":/icons/icons8-intestine-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.mainUpgradeIcon_4.setIcon(icon6)
		self.mainUpgradeIcon_4.setIconSize(QtCore.QSize(40, 40))
		self.mainUpgradeIcon_4.setFlat(True)
		self.mainUpgradeIcon_4.setObjectName("mainUpgradeIcon_4")
		self.horizontalLayout_6.addWidget(self.mainUpgradeIcon_4)
		self.mainUpgradeName_4 = QtWidgets.QLabel(self.mainUpgrade_4)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.mainUpgradeName_4.setFont(font)
		self.mainUpgradeName_4.setObjectName("mainUpgradeName_4")
		self.horizontalLayout_6.addWidget(self.mainUpgradeName_4)
		self.mainUpgradeBuy_4 = QtWidgets.QPushButton(self.mainUpgrade_4)
		self.mainUpgradeBuy_4.setMinimumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_4.setMaximumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.mainUpgradeBuy_4.setIcon(icon3)
		self.mainUpgradeBuy_4.setObjectName("mainUpgradeBuy_4")
		self.horizontalLayout_6.addWidget(self.mainUpgradeBuy_4)
		self.verticalLayout_4.addWidget(self.mainUpgrade_4)
		self.mainUpgrade_5 = QtWidgets.QFrame(self.mainUpgradeFrame)
		self.mainUpgrade_5.setEnabled(False)
		self.mainUpgrade_5.setMinimumSize(QtCore.QSize(0, 100))
		self.mainUpgrade_5.setMaximumSize(QtCore.QSize(16777215, 100))
		self.mainUpgrade_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgrade_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgrade_5.setObjectName("mainUpgrade_5")
		self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.mainUpgrade_5)
		self.horizontalLayout_9.setObjectName("horizontalLayout_9")
		self.mainUpgradeIcon_5 = QtWidgets.QPushButton(self.mainUpgrade_5)
		self.mainUpgradeIcon_5.setMinimumSize(QtCore.QSize(50, 0))
		self.mainUpgradeIcon_5.setMaximumSize(QtCore.QSize(50, 16777215))
		icon7 = QtGui.QIcon()
		icon7.addPixmap(QtGui.QPixmap(":/icons/icons8-savouring-delicious-food-face-48.png"), QtGui.QIcon.Normal,
		                QtGui.QIcon.Off)
		self.mainUpgradeIcon_5.setIcon(icon7)
		self.mainUpgradeIcon_5.setIconSize(QtCore.QSize(40, 40))
		self.mainUpgradeIcon_5.setFlat(True)
		self.mainUpgradeIcon_5.setObjectName("mainUpgradeIcon_5")
		self.horizontalLayout_9.addWidget(self.mainUpgradeIcon_5)
		self.mainUpgradeName_5 = QtWidgets.QLabel(self.mainUpgrade_5)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.mainUpgradeName_5.setFont(font)
		self.mainUpgradeName_5.setObjectName("mainUpgradeName_5")
		self.horizontalLayout_9.addWidget(self.mainUpgradeName_5)
		self.mainUpgradeBuy_5 = QtWidgets.QPushButton(self.mainUpgrade_5)
		self.mainUpgradeBuy_5.setMinimumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_5.setMaximumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.mainUpgradeBuy_5.setIcon(icon3)
		self.mainUpgradeBuy_5.setObjectName("mainUpgradeBuy_5")
		self.horizontalLayout_9.addWidget(self.mainUpgradeBuy_5)
		self.verticalLayout_4.addWidget(self.mainUpgrade_5)
		self.mainUpgrade_6 = QtWidgets.QFrame(self.mainUpgradeFrame)
		self.mainUpgrade_6.setEnabled(False)
		self.mainUpgrade_6.setMinimumSize(QtCore.QSize(0, 100))
		self.mainUpgrade_6.setMaximumSize(QtCore.QSize(16777215, 100))
		self.mainUpgrade_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.mainUpgrade_6.setFrameShadow(QtWidgets.QFrame.Raised)
		self.mainUpgrade_6.setObjectName("mainUpgrade_6")
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.mainUpgrade_6)
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.mainUpgradeIcon_6 = QtWidgets.QPushButton(self.mainUpgrade_6)
		self.mainUpgradeIcon_6.setMinimumSize(QtCore.QSize(50, 0))
		self.mainUpgradeIcon_6.setMaximumSize(QtCore.QSize(50, 16777215))
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap(":/icons/icons8-burger-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.mainUpgradeIcon_6.setIcon(icon8)
		self.mainUpgradeIcon_6.setIconSize(QtCore.QSize(40, 40))
		self.mainUpgradeIcon_6.setFlat(True)
		self.mainUpgradeIcon_6.setObjectName("mainUpgradeIcon_6")
		self.horizontalLayout_7.addWidget(self.mainUpgradeIcon_6)
		self.mainUpgradeName_6 = QtWidgets.QLabel(self.mainUpgrade_6)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.mainUpgradeName_6.setFont(font)
		self.mainUpgradeName_6.setObjectName("mainUpgradeName_6")
		self.horizontalLayout_7.addWidget(self.mainUpgradeName_6)
		self.mainUpgradeBuy_6 = QtWidgets.QPushButton(self.mainUpgrade_6)
		self.mainUpgradeBuy_6.setMinimumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_6.setMaximumSize(QtCore.QSize(130, 60))
		self.mainUpgradeBuy_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.mainUpgradeBuy_6.setIcon(icon3)
		self.mainUpgradeBuy_6.setObjectName("mainUpgradeBuy_6")
		self.horizontalLayout_7.addWidget(self.mainUpgradeBuy_6)
		self.verticalLayout_4.addWidget(self.mainUpgrade_6)
		self.horizontalLayout_2.addWidget(self.mainUpgradeFrame)
		self.helpUpgradeFrame = QtWidgets.QFrame(self.mainUpgradeMenuFrame)
		self.helpUpgradeFrame.setMaximumSize(QtCore.QSize(0, 16777215))
		self.helpUpgradeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.helpUpgradeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.helpUpgradeFrame.setObjectName("helpUpgradeFrame")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.helpUpgradeFrame)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.helpUpgrade = QtWidgets.QFrame(self.helpUpgradeFrame)
		self.helpUpgrade.setEnabled(False)
		self.helpUpgrade.setMinimumSize(QtCore.QSize(0, 100))
		self.helpUpgrade.setMaximumSize(QtCore.QSize(16777215, 100))
		self.helpUpgrade.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.helpUpgrade.setFrameShadow(QtWidgets.QFrame.Raised)
		self.helpUpgrade.setObjectName("helpUpgrade")
		self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.helpUpgrade)
		self.horizontalLayout_16.setObjectName("horizontalLayout_16")
		self.helpUpgradeIcon = QtWidgets.QPushButton(self.helpUpgrade)
		self.helpUpgradeIcon.setMinimumSize(QtCore.QSize(50, 0))
		self.helpUpgradeIcon.setMaximumSize(QtCore.QSize(50, 16777215))
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap(":/icons/icons8-crying-baby-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.helpUpgradeIcon.setIcon(icon9)
		self.helpUpgradeIcon.setIconSize(QtCore.QSize(40, 40))
		self.helpUpgradeIcon.setAutoDefault(False)
		self.helpUpgradeIcon.setFlat(True)
		self.helpUpgradeIcon.setObjectName("helpUpgradeIcon")
		self.horizontalLayout_16.addWidget(self.helpUpgradeIcon)
		self.helpUpgradeName = QtWidgets.QLabel(self.helpUpgrade)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		self.helpUpgradeName.setFont(font)
		self.helpUpgradeName.setObjectName("helpUpgradeName")
		self.horizontalLayout_16.addWidget(self.helpUpgradeName)
		self.helpUpgradeBuy = QtWidgets.QPushButton(self.helpUpgrade)
		self.helpUpgradeBuy.setMinimumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy.setMaximumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpUpgradeBuy.setIcon(icon3)
		self.helpUpgradeBuy.setObjectName("helpUpgradeBuy")
		self.horizontalLayout_16.addWidget(self.helpUpgradeBuy)
		self.verticalLayout_5.addWidget(self.helpUpgrade)
		self.helpUpgrade_2 = QtWidgets.QFrame(self.helpUpgradeFrame)
		self.helpUpgrade_2.setEnabled(False)
		self.helpUpgrade_2.setMinimumSize(QtCore.QSize(0, 100))
		self.helpUpgrade_2.setMaximumSize(QtCore.QSize(16777215, 100))
		self.helpUpgrade_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.helpUpgrade_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.helpUpgrade_2.setObjectName("helpUpgrade_2")
		self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.helpUpgrade_2)
		self.horizontalLayout_17.setObjectName("horizontalLayout_17")
		self.helpUpgradeIcon_2 = QtWidgets.QPushButton(self.helpUpgrade_2)
		self.helpUpgradeIcon_2.setMinimumSize(QtCore.QSize(50, 0))
		self.helpUpgradeIcon_2.setMaximumSize(QtCore.QSize(50, 16777215))
		icon10 = QtGui.QIcon()
		icon10.addPixmap(QtGui.QPixmap(":/icons/icons8-student-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.helpUpgradeIcon_2.setIcon(icon10)
		self.helpUpgradeIcon_2.setIconSize(QtCore.QSize(40, 40))
		self.helpUpgradeIcon_2.setFlat(True)
		self.helpUpgradeIcon_2.setObjectName("helpUpgradeIcon_2")
		self.horizontalLayout_17.addWidget(self.helpUpgradeIcon_2)
		self.helpUpgradeName_2 = QtWidgets.QLabel(self.helpUpgrade_2)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		self.helpUpgradeName_2.setFont(font)
		self.helpUpgradeName_2.setObjectName("helpUpgradeName_2")
		self.horizontalLayout_17.addWidget(self.helpUpgradeName_2)
		self.helpUpgradeBuy_2 = QtWidgets.QPushButton(self.helpUpgrade_2)
		self.helpUpgradeBuy_2.setMinimumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_2.setMaximumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpUpgradeBuy_2.setIcon(icon3)
		self.helpUpgradeBuy_2.setObjectName("helpUpgradeBuy_2")
		self.horizontalLayout_17.addWidget(self.helpUpgradeBuy_2)
		self.verticalLayout_5.addWidget(self.helpUpgrade_2)
		self.helpUpgrade_3 = QtWidgets.QFrame(self.helpUpgradeFrame)
		self.helpUpgrade_3.setEnabled(False)
		self.helpUpgrade_3.setMinimumSize(QtCore.QSize(0, 100))
		self.helpUpgrade_3.setMaximumSize(QtCore.QSize(16777215, 100))
		self.helpUpgrade_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.helpUpgrade_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.helpUpgrade_3.setObjectName("helpUpgrade_3")
		self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.helpUpgrade_3)
		self.horizontalLayout_20.setObjectName("horizontalLayout_20")
		self.helpUpgradeIcon_3 = QtWidgets.QPushButton(self.helpUpgrade_3)
		self.helpUpgradeIcon_3.setMinimumSize(QtCore.QSize(50, 0))
		self.helpUpgradeIcon_3.setMaximumSize(QtCore.QSize(50, 16777215))
		icon11 = QtGui.QIcon()
		icon11.addPixmap(QtGui.QPixmap(":/icons/icons8-worker-60.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.helpUpgradeIcon_3.setIcon(icon11)
		self.helpUpgradeIcon_3.setIconSize(QtCore.QSize(40, 40))
		self.helpUpgradeIcon_3.setFlat(True)
		self.helpUpgradeIcon_3.setObjectName("helpUpgradeIcon_3")
		self.horizontalLayout_20.addWidget(self.helpUpgradeIcon_3)
		self.helpUpgradeName_3 = QtWidgets.QLabel(self.helpUpgrade_3)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		self.helpUpgradeName_3.setFont(font)
		self.helpUpgradeName_3.setObjectName("helpUpgradeName_3")
		self.horizontalLayout_20.addWidget(self.helpUpgradeName_3)
		self.helpUpgradeBuy_3 = QtWidgets.QPushButton(self.helpUpgrade_3)
		self.helpUpgradeBuy_3.setMinimumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_3.setMaximumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpUpgradeBuy_3.setIcon(icon3)
		self.helpUpgradeBuy_3.setObjectName("helpUpgradeBuy_3")
		self.horizontalLayout_20.addWidget(self.helpUpgradeBuy_3)
		self.verticalLayout_5.addWidget(self.helpUpgrade_3)
		self.helpUpgrade_4 = QtWidgets.QFrame(self.helpUpgradeFrame)
		self.helpUpgrade_4.setEnabled(False)
		self.helpUpgrade_4.setMinimumSize(QtCore.QSize(0, 100))
		self.helpUpgrade_4.setMaximumSize(QtCore.QSize(16777215, 100))
		self.helpUpgrade_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.helpUpgrade_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.helpUpgrade_4.setObjectName("helpUpgrade_4")
		self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.helpUpgrade_4)
		self.horizontalLayout_21.setObjectName("horizontalLayout_21")
		self.helpUpgradeIcon_4 = QtWidgets.QPushButton(self.helpUpgrade_4)
		self.helpUpgradeIcon_4.setMinimumSize(QtCore.QSize(50, 0))
		self.helpUpgradeIcon_4.setMaximumSize(QtCore.QSize(50, 16777215))
		icon12 = QtGui.QIcon()
		icon12.addPixmap(QtGui.QPixmap(":/icons/icons8-eating-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.helpUpgradeIcon_4.setIcon(icon12)
		self.helpUpgradeIcon_4.setIconSize(QtCore.QSize(40, 40))
		self.helpUpgradeIcon_4.setFlat(True)
		self.helpUpgradeIcon_4.setObjectName("helpUpgradeIcon_4")
		self.horizontalLayout_21.addWidget(self.helpUpgradeIcon_4)
		self.helpUpgradeName_4 = QtWidgets.QLabel(self.helpUpgrade_4)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		self.helpUpgradeName_4.setFont(font)
		self.helpUpgradeName_4.setObjectName("helpUpgradeName_4")
		self.horizontalLayout_21.addWidget(self.helpUpgradeName_4)
		self.helpUpgradeBuy_4 = QtWidgets.QPushButton(self.helpUpgrade_4)
		self.helpUpgradeBuy_4.setMinimumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_4.setMaximumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpUpgradeBuy_4.setIcon(icon3)
		self.helpUpgradeBuy_4.setObjectName("helpUpgradeBuy_4")
		self.horizontalLayout_21.addWidget(self.helpUpgradeBuy_4)
		self.verticalLayout_5.addWidget(self.helpUpgrade_4)
		self.helpUpgrade_5 = QtWidgets.QFrame(self.helpUpgradeFrame)
		self.helpUpgrade_5.setEnabled(False)
		self.helpUpgrade_5.setMinimumSize(QtCore.QSize(0, 100))
		self.helpUpgrade_5.setMaximumSize(QtCore.QSize(16777215, 100))
		self.helpUpgrade_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.helpUpgrade_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.helpUpgrade_5.setObjectName("helpUpgrade_5")
		self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.helpUpgrade_5)
		self.horizontalLayout_18.setObjectName("horizontalLayout_18")
		self.helpUpgradeIcon_5 = QtWidgets.QPushButton(self.helpUpgrade_5)
		self.helpUpgradeIcon_5.setMinimumSize(QtCore.QSize(50, 0))
		self.helpUpgradeIcon_5.setMaximumSize(QtCore.QSize(50, 16777215))
		icon13 = QtGui.QIcon()
		icon13.addPixmap(QtGui.QPixmap(":/icons/fat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.helpUpgradeIcon_5.setIcon(icon13)
		self.helpUpgradeIcon_5.setIconSize(QtCore.QSize(40, 40))
		self.helpUpgradeIcon_5.setFlat(True)
		self.helpUpgradeIcon_5.setObjectName("helpUpgradeIcon_5")
		self.horizontalLayout_18.addWidget(self.helpUpgradeIcon_5)
		self.helpUpgradeName_5 = QtWidgets.QLabel(self.helpUpgrade_5)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		self.helpUpgradeName_5.setFont(font)
		self.helpUpgradeName_5.setObjectName("helpUpgradeName_5")
		self.horizontalLayout_18.addWidget(self.helpUpgradeName_5)
		self.helpUpgradeBuy_5 = QtWidgets.QPushButton(self.helpUpgrade_5)
		self.helpUpgradeBuy_5.setMinimumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_5.setMaximumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpUpgradeBuy_5.setIcon(icon3)
		self.helpUpgradeBuy_5.setObjectName("helpUpgradeBuy_5")
		self.horizontalLayout_18.addWidget(self.helpUpgradeBuy_5)
		self.verticalLayout_5.addWidget(self.helpUpgrade_5)
		self.helpUpgrade_6 = QtWidgets.QFrame(self.helpUpgradeFrame)
		self.helpUpgrade_6.setEnabled(False)
		self.helpUpgrade_6.setMinimumSize(QtCore.QSize(0, 100))
		self.helpUpgrade_6.setMaximumSize(QtCore.QSize(16777215, 100))
		font = QtGui.QFont()
		self.helpUpgrade_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.helpUpgrade_6.setFrameShadow(QtWidgets.QFrame.Raised)
		self.helpUpgrade_6.setObjectName("helpUpgrade_6")
		self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.helpUpgrade_6)
		self.horizontalLayout_19.setObjectName("horizontalLayout_19")
		self.helpUpgradeIcon_6 = QtWidgets.QPushButton(self.helpUpgrade_6)
		self.helpUpgradeIcon_6.setMinimumSize(QtCore.QSize(50, 0))
		self.helpUpgradeIcon_6.setMaximumSize(QtCore.QSize(50, 16777215))
		font = QtGui.QFont()
		icon14 = QtGui.QIcon()
		icon14.addPixmap(QtGui.QPixmap(":/icons/fat_guy-removebg-preview (1) (1).png"), QtGui.QIcon.Normal,
		                 QtGui.QIcon.Off)
		self.helpUpgradeIcon_6.setIcon(icon14)
		self.helpUpgradeIcon_6.setIconSize(QtCore.QSize(40, 40))
		self.helpUpgradeIcon_6.setFlat(True)
		self.helpUpgradeIcon_6.setObjectName("helpUpgradeIcon_6")
		self.horizontalLayout_19.addWidget(self.helpUpgradeIcon_6)
		self.helpUpgradeName_6 = QtWidgets.QLabel(self.helpUpgrade_6)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		self.helpUpgradeName_6.setFont(font)
		self.helpUpgradeName_6.setObjectName("helpUpgradeName_6")
		self.horizontalLayout_19.addWidget(self.helpUpgradeName_6)
		self.helpUpgradeBuy_6 = QtWidgets.QPushButton(self.helpUpgrade_6)
		self.helpUpgradeBuy_6.setMinimumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_6.setMaximumSize(QtCore.QSize(130, 60))
		self.helpUpgradeBuy_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.helpUpgradeBuy_6.setIcon(icon3)
		self.helpUpgradeBuy_6.setObjectName("helpUpgradeBuy_6")
		self.horizontalLayout_19.addWidget(self.helpUpgradeBuy_6)
		self.verticalLayout_5.addWidget(self.helpUpgrade_6)
		self.horizontalLayout_2.addWidget(self.helpUpgradeFrame)
		self.verticalLayout.addWidget(self.mainUpgradeMenuFrame)
		self.settingsFrame = QtWidgets.QFrame(self.centralwidget)
		self.settingsFrame.setGeometry(QtCore.QRect(10, 710, 62, 61))
		self.settingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.settingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.settingsFrame.setObjectName("settingsFrame")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settingsFrame)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.settingsMenuButton = QtWidgets.QPushButton(self.settingsFrame)
		self.settingsMenuButton.setMinimumSize(QtCore.QSize(50, 50))
		self.settingsMenuButton.setMaximumSize(QtCore.QSize(50, 50))
		icon15 = QtGui.QIcon()
		icon15.addPixmap(QtGui.QPixmap("images/icons/icons8-settings-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.settingsMenuButton.setIcon(icon15)
		self.settingsMenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.settingsMenuButton.setIconSize(QtCore.QSize(30, 30))
		self.settingsMenuButton.setObjectName("settingsMenuButton")
		self.verticalLayout_6.addWidget(self.settingsMenuButton)
		self.githubFrame = QtWidgets.QFrame(self.centralwidget)
		self.githubFrame.setGeometry(QtCore.QRect(75, 710, 62, 61))
		self.githubFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.githubFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.githubFrame.setObjectName("githubFrame")
		self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.githubFrame)
		self.verticalLayout_17.setObjectName("verticalLayout_17")
		self.githubButton = QtWidgets.QPushButton(self.githubFrame)
		self.githubButton.setMinimumSize(QtCore.QSize(50, 50))
		self.githubButton.setMaximumSize(QtCore.QSize(50, 50))
		icon22 = QtGui.QIcon()
		icon22.addPixmap(QtGui.QPixmap(":/icons/icons8-github-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.githubButton.setIcon(icon22)
		self.githubButton.setIconSize(QtCore.QSize(35, 35))
		self.githubButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.githubButton.setObjectName("githubButton")
		self.verticalLayout_17.addWidget(self.githubButton)
		self.telegramFrame = QtWidgets.QFrame(self.centralwidget)
		self.telegramFrame.setGeometry(QtCore.QRect(140, 710, 62, 61))
		self.telegramFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.telegramFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.telegramFrame.setObjectName("telegramFrame")
		self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.telegramFrame)
		self.verticalLayout_18.setObjectName("verticalLayout_18")
		self.telegramButton = QtWidgets.QPushButton(self.telegramFrame)
		self.telegramButton.setMinimumSize(QtCore.QSize(50, 50))
		self.telegramButton.setMaximumSize(QtCore.QSize(50, 50))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		self.telegramButton.setFont(font)
		icon23 = QtGui.QIcon()
		icon23.addPixmap(QtGui.QPixmap(":/icons/icons8-telegram-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.telegramButton.setIcon(icon23)
		self.telegramButton.setIconSize(QtCore.QSize(35, 35))
		self.telegramButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.telegramButton.setObjectName("telegramButton")
		self.verticalLayout_18.addWidget(self.telegramButton)
		self.clickerFrame = QtWidgets.QFrame(self.centralwidget)
		self.clickerFrame.setGeometry(QtCore.QRect(10, 143, 581, 561))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.clickerFrame.setFont(font)
		self.clickerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.clickerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.clickerFrame.setObjectName("clickerFrame")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.clickerFrame)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.nameLabel = QtWidgets.QLabel(self.clickerFrame)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
		self.nameLabel.setSizePolicy(sizePolicy)
		self.nameLabel.setMinimumSize(QtCore.QSize(0, 70))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.nameLabel.setFont(font)
		self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.nameLabel.setObjectName("nameLabel")
		self.verticalLayout_3.addWidget(self.nameLabel)
		self.burgerButton = QtWidgets.QPushButton(self.clickerFrame)
		self.burgerButton.setEnabled(True)
		self.burgerButton.setGraphicsEffect(self.shadow_effect)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.burgerButton.sizePolicy().hasHeightForWidth())
		self.burgerButton.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.burgerButton.setFont(font)
		self.burgerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.burgerButton.setAutoFillBackground(False)
		icon16 = QtGui.QIcon()
		icon16.addPixmap(QtGui.QPixmap(f"images/imgs/бургер{self.stats[13]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.burgerButton.setIcon(self.BurgerIcon)
		self.burgerButton.setIconSize(QtCore.QSize(450, 450))
		self.burgerButton.setFlat(True)
		self.burgerButton.setObjectName("burgerButton")
		self.verticalLayout_3.addWidget(self.burgerButton)
		self.statisticsFrame = QtWidgets.QFrame(self.centralwidget)
		self.statisticsFrame.setGeometry(QtCore.QRect(10, 10, 581, 121))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.statisticsFrame.setFont(font)
		self.statisticsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.statisticsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.statisticsFrame.setObjectName("statisticsFrame")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.statisticsFrame)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.countLabel = QtWidgets.QLabel(self.statisticsFrame)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.countLabel.setFont(font)
		self.countLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.countLabel.setObjectName("countLabel")
		self.verticalLayout_2.addWidget(self.countLabel)
		self.helpCountLabel = QtWidgets.QLabel(self.statisticsFrame)
		self.helpCountLabel.setMaximumSize(QtCore.QSize(16777215, 30))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(False)
		font.setWeight(50)
		self.helpCountLabel.setFont(font)
		self.helpCountLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.helpCountLabel.setObjectName("helpCountLabel")
		self.verticalLayout_2.addWidget(self.helpCountLabel)
		self.settings = QtWidgets.QFrame(self.centralwidget)
		
		self.settings.setEnabled(True)
		self.settings.setGeometry(QtCore.QRect(0, 0, 0, 780))
		self.settings.setMinimumSize(QtCore.QSize(0, 780))
		self.settings.setMaximumSize(QtCore.QSize(1037, 780))
		self.settings.setToolTipDuration(0)
		self.settings.setObjectName("settings")
		self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.settings)
		self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.settingsWrapper = QtWidgets.QFrame(self.settings)
		self.settingsWrapper.setMinimumSize(QtCore.QSize(518, 0))
		self.settingsWrapper.setMaximumSize(QtCore.QSize(518, 16777215))
		self.settingsWrapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.settingsWrapper.setFrameShadow(QtWidgets.QFrame.Raised)
		self.settingsWrapper.setObjectName("settingsWrapper")
		self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.settingsWrapper)
		self.verticalLayout_14.setObjectName("verticalLayout_14")
		self.settingsLabelWrapper = QtWidgets.QFrame(self.settingsWrapper)
		self.settingsLabelWrapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.settingsLabelWrapper.setFrameShadow(QtWidgets.QFrame.Raised)
		self.settingsLabelWrapper.setObjectName("settingsLabelWrapper")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.settingsLabelWrapper)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.settingsLabel = QtWidgets.QLabel(self.settingsLabelWrapper)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.settingsLabel.setFont(font)
		self.settingsLabel.setObjectName("settingsLabel")
		self.verticalLayout_8.addWidget(self.settingsLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
		self.verticalLayout_14.addWidget(self.settingsLabelWrapper, 0, QtCore.Qt.AlignHCenter)
		self.frame_3 = QtWidgets.QFrame(self.settingsWrapper)
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
		self.verticalLayout_9.setObjectName("verticalLayout_9")
		self.volumeLabel = QtWidgets.QLabel(self.frame_3)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.volumeLabel.setFont(font)
		self.volumeLabel.setObjectName("volumeLabel")
		self.volumeLabel.setStyleSheet("padding: 20px;")
		self.verticalLayout_9.addWidget(self.volumeLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
		self.muteButton = QtWidgets.QPushButton(self.frame_3)
		self.muteButton.setMinimumSize(QtCore.QSize(150, 60))
		if not self.stats[32]:
			self.iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-mute-100.png"))
			self.muteButton.setText("ВЫКЛЮЧИТЬ")
		else:
			self.iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-volume-100.png"))
			self.muteButton.setText("ВКЛЮЧИТЬ")
		self.muteButton.setIcon(self.iconMute)
		self.muteButton.setIconSize(QtCore.QSize(35, 35))
		self.muteButton.setObjectName("pushButton")
		self.verticalLayout_9.addWidget(self.muteButton, 0, QtCore.Qt.AlignHCenter)
		self.verticalLayout_14.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
		self.frame_6 = QtWidgets.QFrame(self.settingsWrapper)
		self.frame_6.setMinimumSize(QtCore.QSize(459, 350))
		self.frame_6.setMaximumSize(QtCore.QSize(450, 400))
		self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_6.setObjectName("frame_6")
		self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_6)
		self.verticalLayout_11.setObjectName("verticalLayout_11")
		self.statisticsLabel = QtWidgets.QLabel(self.frame_6)
		self.statisticsLabel.setMaximumSize(QtCore.QSize(16777215, 100))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setBold(True)
		font.setWeight(75)
		self.statisticsLabel.setFont(font)
		self.statisticsLabel.setObjectName("statisticsLabel")
		self.verticalLayout_11.addWidget(self.statisticsLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
		self.statisticsToolBox = QtWidgets.QToolBox(self.frame_6)
		self.statisticsToolBox.setMaximumSize(QtCore.QSize(16777215, 300))
		self.statisticsToolBox.setObjectName("statisticsToolBox")
		self.page = QtWidgets.QWidget()
		self.page.setGeometry(QtCore.QRect(0, 0, 422, 312))
		self.page.setObjectName("page")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		self.actualCountLabel = QtWidgets.QLabel(self.page)
		self.actualCountLabel.setObjectName("actualCountLabel")
		self.verticalLayout_10.addWidget(self.actualCountLabel)
		self.allCountLabel = QtWidgets.QLabel(self.page)
		self.allCountLabel.setObjectName("allCountLabel")
		self.verticalLayout_10.addWidget(self.allCountLabel)
		self.clickPowerLabel = QtWidgets.QLabel(self.page)
		self.clickPowerLabel.setObjectName("allCiclPowerLabel")
		self.verticalLayout_10.addWidget(self.clickPowerLabel)
		self.allUpgradesLabel = QtWidgets.QLabel(self.page)
		self.allUpgradesLabel.setObjectName("allUpgradesLabel")
		self.verticalLayout_10.addWidget(self.allUpgradesLabel)
		self.allMainUpgradesLabel = QtWidgets.QLabel(self.page)
		self.allMainUpgradesLabel.setObjectName("allMainUpgradesLabel")
		self.verticalLayout_10.addWidget(self.allMainUpgradesLabel)
		self.allHelpUpgradesLabel = QtWidgets.QLabel(self.page)
		self.allHelpUpgradesLabel.setObjectName("allHelpUpgradesLabel")
		self.verticalLayout_10.addWidget(self.allHelpUpgradesLabel)
		self.gameSessionTimeLabel = QtWidgets.QLabel(self.page)
		self.gameSessionTimeLabel.setObjectName("gameSessionTimeLabel")
		self.verticalLayout_10.addWidget(self.gameSessionTimeLabel)
		icon18 = QtGui.QIcon()
		icon18.addPixmap(QtGui.QPixmap(":/icons/icons8-down-button-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.statisticsToolBox.addItem(self.page, icon18, "")
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setGeometry(QtCore.QRect(0, 0, 439, 240))
		self.page_2.setObjectName("page_2")
		icon19 = QtGui.QIcon()
		icon19.addPixmap(QtGui.QPixmap(":/icons/icons8-slide-up-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.statisticsToolBox.addItem(self.page_2, icon19, "")
		self.verticalLayout_11.addWidget(self.statisticsToolBox)
		self.verticalLayout_14.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
		self.frame_5 = QtWidgets.QFrame(self.settingsWrapper)
		self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_5.setObjectName("frame_5")
		self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_5)
		self.verticalLayout_12.setObjectName("verticalLayout_12")
		self.returnButton = QtWidgets.QPushButton(self.frame_5)
		self.returnButton.setMinimumSize(QtCore.QSize(150, 60))
		icon20 = QtGui.QIcon()
		icon20.addPixmap(QtGui.QPixmap(":/icons/icons8-return-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.returnButton.setIcon(icon20)
		self.returnButton.setIconSize(QtCore.QSize(35, 35))
		self.returnButton.setObjectName("returnButton")
		self.verticalLayout_12.addWidget(self.returnButton)
		self.verticalLayout_14.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
		self.frame_4 = QtWidgets.QFrame(self.settingsWrapper)
		self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_4.setObjectName("frame_4")
		self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_4)
		self.verticalLayout_13.setObjectName("verticalLayout_13")
		self.saveAndExitButton = QtWidgets.QPushButton(self.frame_4)
		self.saveAndExitButton.setMinimumSize(QtCore.QSize(150, 60))
		icon21 = QtGui.QIcon()
		icon21.addPixmap(QtGui.QPixmap(":/icons/icons8-close-window-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.saveAndExitButton.setIcon(icon21)
		self.saveAndExitButton.setIconSize(QtCore.QSize(35, 35))
		self.saveAndExitButton.setObjectName("saveButton")
		self.saveAndExitButton.setStyleSheet('padding: 0 10px;')
		self.verticalLayout_13.addWidget(self.saveAndExitButton, 0, QtCore.Qt.AlignTop)
		self.verticalLayout_14.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
		self.verticalLayout_7.addWidget(self.settingsWrapper, 0, QtCore.Qt.AlignHCenter)
		self.retranslateUi(BurgerClicker)
		self.statisticsToolBox.setCurrentIndex(0)
		BurgerClicker.setCentralWidget(self.centralwidget)
		QtCore.QMetaObject.connectSlotsByName(BurgerClicker)
	
	def retranslateUi(self, BurgerClicker):
		_translate = QtCore.QCoreApplication.translate
		BurgerClicker.setWindowTitle(_translate("BurgerClicker", "Burger Clicker"))
		self.upgradesButton.setText(_translate("BurgerClicker", "Улучшения"))
		self.helpsButton.setText(_translate("BurgerClicker", "Помощники"))
		self.mainUpgradeName.setText(_translate("BurgerClicker", f"Размер рта X {self.stats[8]}"))
		self.mainUpgradeBuy.setText(_translate("BurgerClicker", f"{self.stats[20]} бургеров"))
		self.mainUpgradeName_2.setText(_translate("BurgerClicker", f"Мощность челюсти X {self.stats[9]}"))
		self.mainUpgradeBuy_2.setText(_translate("BurgerClicker", f"{self.stats[21]} бургеров"))
		self.mainUpgradeName_3.setText(_translate("BurgerClicker", f"Объем желудка X {self.stats[10]}"))
		self.mainUpgradeBuy_3.setText(_translate("BurgerClicker", f"{self.stats[22]} бургеров"))
		self.mainUpgradeName_4.setText(_translate("BurgerClicker", f"Сила кишки X {self.stats[11]}"))
		self.mainUpgradeBuy_4.setText(_translate("BurgerClicker", f"{self.stats[23]} бургеров"))
		self.mainUpgradeName_5.setText(_translate("BurgerClicker", f"Аппетит X {self.stats[12]}"))
		self.mainUpgradeBuy_5.setText(_translate("BurgerClicker", f"{self.stats[24]} бургеров"))
		self.mainUpgradeName_6.setText(_translate("BurgerClicker", f"Уровень бургера (ур. {self.stats[13]})"))
		self.mainUpgradeBuy_6.setText(_translate("BurgerClicker", f"{self.stats[25]} бургеров"))
		self.helpUpgradeName.setText(_translate("BurgerClicker", f"Капризный ребенок X {self.stats[14]}"))
		self.helpUpgradeBuy.setText(_translate("BurgerClicker", f"{self.stats[26]} бургеров"))
		self.helpUpgradeName_2.setText(_translate("BurgerClicker", f"Бедный студент X {self.stats[15]}"))
		self.helpUpgradeBuy_2.setText(_translate("BurgerClicker", f"{self.stats[27]} бургеров"))
		self.helpUpgradeName_3.setText(_translate("BurgerClicker", f"Уставший работяга X {self.stats[16]}"))
		self.helpUpgradeBuy_3.setText(_translate("BurgerClicker", f"{self.stats[28]} бургеров"))
		self.helpUpgradeName_4.setText(_translate("BurgerClicker", f"Любитель поесть X {self.stats[17]}"))
		self.helpUpgradeBuy_4.setText(_translate("BurgerClicker", f"{self.stats[29]} бургеров"))
		self.helpUpgradeName_5.setText(_translate("BurgerClicker", f"Голодный толстяк X {self.stats[18]}"))
		self.helpUpgradeBuy_5.setText(_translate("BurgerClicker", f"{self.stats[30]} бургеров"))
		self.helpUpgradeName_6.setText(_translate("BurgerClicker", f"Америкос X {self.stats[19]}"))
		self.helpUpgradeBuy_6.setText(_translate("BurgerClicker", f"{self.stats[31]} бургеров"))
		self.nameLabel.setText(_translate("BurgerClicker", self.burger_names_list[self.stats[13]-1]))
		self.countLabel.setText(_translate("BurgerClicker", f"Съедено: {self.stats[0]} бургеров"))
		self.helpCountLabel.setText(_translate("BurgerClicker", f"Помощь: {self.stats[1]}/сек"))
		self.settingsLabel.setText(_translate("BurgerClicker", "НАСТРОЙКИ"))
		self.volumeLabel.setText(_translate("BurgerClicker", "ЗВУК"))
		self.statisticsLabel.setText(_translate("BurgerClicker", "СТАТИСТИКА"))
		self.actualCountLabel.setText(
			_translate("BurgerClicker", f"Актуальное количество съеденных бургеров: {self.stats[0]}"))
		self.allCountLabel.setText(_translate("BurgerClicker", f"Общее количество съеденных бургеров {self.stats[3]}"))
		self.clickPowerLabel.setText(_translate("BurgerClicker", f"Сила клика: {self.stats[2]}"))
		self.allUpgradesLabel.setText(_translate("BurgerClicker", f"Общее количество улучшений: {self.stats[4]}"))
		self.allMainUpgradesLabel.setText(
			_translate("BurgerClicker", f"Количество улучшений клика: {self.stats[5]}"))
		self.gameSessionTimeLabel.setText(
			_translate("BurgerClicker", f"Время, проведенное в игре с запуска: {self.stats[6]}"))
		self.allHelpUpgradesLabel.setText(
			_translate("BurgerClicker", f"Количество улучшений помощников: {self.stats[7]}"))
		self.statisticsToolBox.setItemText(self.statisticsToolBox.indexOf(self.page),
		                                   _translate("BurgerClicker", "ОТКРЫТЬ СТАТИСТИКУ"))
		self.statisticsToolBox.setItemText(self.statisticsToolBox.indexOf(self.page_2),
		                                   _translate("BurgerClicker", "ЗАКРЫТЬ СТАТИСТИКУ"))
		self.returnButton.setText(_translate("BurgerClicker", "ВЕРНУТЬСЯ"))
		self.saveAndExitButton.setText(_translate("BurgerClicker", "СОХРАНИТЬ И ВЫЙТИ"))
	
	