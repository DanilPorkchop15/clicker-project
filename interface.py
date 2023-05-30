# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from images.icons_rc import *
from images.imgs_rc import *
import time
from PyQt5.QtMultimedia import QSound
import webbrowser
import threading
import ctypes

myappid = 'PorkchopInc.Burger_Clicker.Burger_Clicker.v1.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Ui_BurgerClicker(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.burger_count = 0.0
        self.helps_speed_count = 0
        self.click_power = 1
        self.allCount = 0
        self.allUpgrades = 0
        self.allMainUpgrades = 0
        self.startTime = time.time()
        self.gameSessionTime = 0
        self.allHelpUpgrades = 0
        self.main_count_1 = 0
        self.main_count_2 = 0
        self.main_count_3 = 0
        self.main_count_4 = 0
        self.main_count_5 = 0
        self.main_count_6 = 1
        self.help_count_1 = 0
        self.help_count_2 = 0
        self.help_count_3 = 0
        self.help_count_4 = 0
        self.help_count_5 = 0
        self.help_count_6 = 0
        self.main_buy_1 = 10
        self.main_buy_2 = 100
        self.main_buy_3 = 300
        self.main_buy_4 = 1000
        self.main_buy_5 = 2500
        self.main_buy_6 = 200
        self.help_buy_1 = 100
        self.help_buy_2 = 500
        self.help_buy_3 = 1000
        self.help_buy_4 = 3000
        self.help_buy_5 = 10000
        self.help_buy_6 = 25000
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
        self.BurgerIcon.addPixmap(QtGui.QPixmap(f":/images/бургер{self.main_count_6}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.telegram_url = 'https://t.me/porkchoppppppp'
        self.github_url = 'https://github.com/DanilPorkchop15'
        self.click_sound = QSound('sfx/click.wav', self)
        self.upgrade_sound = QSound('sfx/upgrade.wav', self)
        self.settings_sound = QSound('sfx/settings.wav', self)
        self.mute = 0

    def setupUi(self, BurgerClicker):
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
"        background-color: rgba(255, 255, 255, 0.1);\n"
"        border: 1px solid gray\n"
"}\n"
"\n"
"\n"
"#helpsButton:pressed, #upgradesButton:pressed{\n"
"        background-color: rgba(0, 100, 0, 0.1);\n"
"        border-top: 2px solid gray\n"
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
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.upgradeFrame = QtWidgets.QFrame(self.centralwidget)
        self.upgradeFrame.setGeometry(QtCore.QRect(600, 10, 431, 761))
        self.upgradeFrame.setMinimumSize(QtCore.QSize(431, 761))
        self.upgradeFrame.setMaximumSize(QtCore.QSize(431, 761))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.upgradeFrame.setFont(font)
        self.upgradeFrame.setStyleSheet("")
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.selectUpgradeFrame.setFont(font)
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.upgradesButton.setFont(font)
        self.upgradesButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-купить-обновление-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upgradesButton.setIcon(icon)
        self.upgradesButton.setIconSize(QtCore.QSize(25, 25))
        self.upgradesButton.setFlat(False)
        self.upgradesButton.setObjectName("upgradesButton")
        self.horizontalLayout.addWidget(self.upgradesButton)
        self.helpsButton = QtWidgets.QPushButton(self.selectUpgradeFrame)
        self.helpsButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.helpsButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons8-связь-и-помощь-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpsButton.setIcon(icon1)
        self.helpsButton.setIconSize(QtCore.QSize(25, 25))
        self.helpsButton.setFlat(False)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgradeMenuFrame.setFont(font)
        self.mainUpgradeMenuFrame.setStyleSheet("")
        self.mainUpgradeMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgradeMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgradeMenuFrame.setObjectName("mainUpgradeMenuFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainUpgradeMenuFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainUpgradeFrame = QtWidgets.QFrame(self.mainUpgradeMenuFrame)
        self.mainUpgradeFrame.setMaximumSize(QtCore.QSize(1234286, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgradeFrame.setFont(font)
        self.mainUpgradeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgradeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgradeFrame.setObjectName("mainUpgradeFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainUpgradeFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mainUpgrade = QtWidgets.QFrame(self.mainUpgradeFrame)
        self.mainUpgrade.setEnabled(False)
        self.mainUpgrade.setMinimumSize(QtCore.QSize(0, 100))
        self.mainUpgrade.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgrade.setFont(font)
        self.mainUpgrade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgrade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgrade.setObjectName("mainUpgrade")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.mainUpgrade)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mainUpgradeIcon = QtWidgets.QPushButton(self.mainUpgrade)
        self.mainUpgradeIcon.setMinimumSize(QtCore.QSize(50, 0))
        self.mainUpgradeIcon.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgradeIcon.setFont(font)
        self.mainUpgradeIcon.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.mainUpgrade_2.setFont(font)
        self.mainUpgrade_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgrade_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgrade_2.setObjectName("mainUpgrade_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainUpgrade_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mainUpgradeIcon_2 = QtWidgets.QPushButton(self.mainUpgrade_2)
        self.mainUpgradeIcon_2.setMinimumSize(QtCore.QSize(50, 0))
        self.mainUpgradeIcon_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.mainUpgradeIcon_2.setFont(font)
        self.mainUpgradeIcon_2.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgrade_3.setFont(font)
        self.mainUpgrade_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgrade_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgrade_3.setObjectName("mainUpgrade_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mainUpgrade_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainUpgradeIcon_3 = QtWidgets.QPushButton(self.mainUpgrade_3)
        self.mainUpgradeIcon_3.setMinimumSize(QtCore.QSize(50, 0))
        self.mainUpgradeIcon_3.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgradeIcon_3.setFont(font)
        self.mainUpgradeIcon_3.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgrade_4.setFont(font)
        self.mainUpgrade_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgrade_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgrade_4.setObjectName("mainUpgrade_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.mainUpgrade_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mainUpgradeIcon_4 = QtWidgets.QPushButton(self.mainUpgrade_4)
        self.mainUpgradeIcon_4.setMinimumSize(QtCore.QSize(50, 0))
        self.mainUpgradeIcon_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgradeIcon_4.setFont(font)
        self.mainUpgradeIcon_4.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.mainUpgrade_5.setFont(font)
        self.mainUpgrade_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgrade_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgrade_5.setObjectName("mainUpgrade_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.mainUpgrade_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mainUpgradeIcon_5 = QtWidgets.QPushButton(self.mainUpgrade_5)
        self.mainUpgradeIcon_5.setMinimumSize(QtCore.QSize(50, 0))
        self.mainUpgradeIcon_5.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.mainUpgradeIcon_5.setFont(font)
        self.mainUpgradeIcon_5.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons8-savouring-delicious-food-face-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainUpgradeIcon_5.setIcon(icon7)
        self.mainUpgradeIcon_5.setIconSize(QtCore.QSize(40, 40))
        self.mainUpgradeIcon_5.setFlat(True)
        self.mainUpgradeIcon_5.setObjectName("mainUpgradeIcon_5")
        self.horizontalLayout_9.addWidget(self.mainUpgradeIcon_5)
        self.mainUpgradeName_5 = QtWidgets.QLabel(self.mainUpgrade_5)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgrade_6.setFont(font)
        self.mainUpgrade_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainUpgrade_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainUpgrade_6.setObjectName("mainUpgrade_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.mainUpgrade_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.mainUpgradeIcon_6 = QtWidgets.QPushButton(self.mainUpgrade_6)
        self.mainUpgradeIcon_6.setMinimumSize(QtCore.QSize(50, 0))
        self.mainUpgradeIcon_6.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mainUpgradeIcon_6.setFont(font)
        self.mainUpgradeIcon_6.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.helpUpgradeFrame.setFont(font)
        self.helpUpgradeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpUpgradeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpUpgradeFrame.setObjectName("helpUpgradeFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.helpUpgradeFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.helpUpgrade = QtWidgets.QFrame(self.helpUpgradeFrame)
        self.helpUpgrade.setEnabled(False)
        self.helpUpgrade.setMinimumSize(QtCore.QSize(0, 100))
        self.helpUpgrade.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgrade.setFont(font)
        self.helpUpgrade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpUpgrade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpUpgrade.setObjectName("helpUpgrade")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.helpUpgrade)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.helpUpgradeIcon = QtWidgets.QPushButton(self.helpUpgrade)
        self.helpUpgradeIcon.setMinimumSize(QtCore.QSize(50, 0))
        self.helpUpgradeIcon.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgradeIcon.setFont(font)
        self.helpUpgradeIcon.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgrade_2.setFont(font)
        self.helpUpgrade_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpUpgrade_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpUpgrade_2.setObjectName("helpUpgrade_2")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.helpUpgrade_2)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.helpUpgradeIcon_2 = QtWidgets.QPushButton(self.helpUpgrade_2)
        self.helpUpgradeIcon_2.setMinimumSize(QtCore.QSize(50, 0))
        self.helpUpgradeIcon_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgradeIcon_2.setFont(font)
        self.helpUpgradeIcon_2.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgrade_3.setFont(font)
        self.helpUpgrade_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpUpgrade_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpUpgrade_3.setObjectName("helpUpgrade_3")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.helpUpgrade_3)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.helpUpgradeIcon_3 = QtWidgets.QPushButton(self.helpUpgrade_3)
        self.helpUpgradeIcon_3.setMinimumSize(QtCore.QSize(50, 0))
        self.helpUpgradeIcon_3.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgradeIcon_3.setFont(font)
        self.helpUpgradeIcon_3.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgrade_4.setFont(font)
        self.helpUpgrade_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpUpgrade_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpUpgrade_4.setObjectName("helpUpgrade_4")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.helpUpgrade_4)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.helpUpgradeIcon_4 = QtWidgets.QPushButton(self.helpUpgrade_4)
        self.helpUpgradeIcon_4.setMinimumSize(QtCore.QSize(50, 0))
        self.helpUpgradeIcon_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgradeIcon_4.setFont(font)
        self.helpUpgradeIcon_4.setText("")
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
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgrade_5.setFont(font)
        self.helpUpgrade_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpUpgrade_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpUpgrade_5.setObjectName("helpUpgrade_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.helpUpgrade_5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.helpUpgradeIcon_5 = QtWidgets.QPushButton(self.helpUpgrade_5)
        self.helpUpgradeIcon_5.setMinimumSize(QtCore.QSize(50, 0))
        self.helpUpgradeIcon_5.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgradeIcon_5.setFont(font)
        self.helpUpgradeIcon_5.setText("")
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
        font.setPointSize(-1)
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
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgrade_6.setFont(font)
        self.helpUpgrade_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.helpUpgrade_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.helpUpgrade_6.setObjectName("helpUpgrade_6")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.helpUpgrade_6)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.helpUpgradeIcon_6 = QtWidgets.QPushButton(self.helpUpgrade_6)
        self.helpUpgradeIcon_6.setMinimumSize(QtCore.QSize(50, 0))
        self.helpUpgradeIcon_6.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.helpUpgradeIcon_6.setFont(font)
        self.helpUpgradeIcon_6.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/fat_guy-removebg-preview (1) (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpUpgradeIcon_6.setIcon(icon14)
        self.helpUpgradeIcon_6.setIconSize(QtCore.QSize(40, 40))
        self.helpUpgradeIcon_6.setFlat(True)
        self.helpUpgradeIcon_6.setObjectName("helpUpgradeIcon_6")
        self.horizontalLayout_19.addWidget(self.helpUpgradeIcon_6)
        self.helpUpgradeName_6 = QtWidgets.QLabel(self.helpUpgrade_6)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
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
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.settingsFrame.setFont(font)
        self.settingsFrame.setStyleSheet("")
        self.settingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsFrame.setObjectName("settingsFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settingsFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.settingsMenuButton = QtWidgets.QPushButton(self.settingsFrame)
        self.settingsMenuButton.setMinimumSize(QtCore.QSize(50, 50))
        self.settingsMenuButton.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.settingsMenuButton.setFont(font)
        self.settingsMenuButton.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/icons/icons8-settings-40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsMenuButton.setIcon(icon15)
        self.settingsMenuButton.setIconSize(QtCore.QSize(30, 30))
        self.settingsMenuButton.setObjectName("settingsMenuButton")
        self.verticalLayout_6.addWidget(self.settingsMenuButton)
        self.githubFrame = QtWidgets.QFrame(self.centralwidget)
        self.githubFrame.setGeometry(QtCore.QRect(75, 710, 62, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.githubFrame.setFont(font)
        self.githubFrame.setStyleSheet("")
        self.githubFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.githubFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.githubFrame.setObjectName("githubFrame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.githubFrame)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.githubButton = QtWidgets.QPushButton(self.githubFrame)
        self.githubButton.setMinimumSize(QtCore.QSize(50, 50))
        self.githubButton.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.githubButton.setFont(font)
        self.githubButton.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/icons8-github-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubButton.setIcon(icon22)
        self.githubButton.setIconSize(QtCore.QSize(35, 35))
        self.githubButton.setObjectName("githubButton")
        self.verticalLayout_17.addWidget(self.githubButton)
        self.telegramFrame = QtWidgets.QFrame(self.centralwidget)
        self.telegramFrame.setGeometry(QtCore.QRect(140, 710, 62, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.telegramFrame.setFont(font)
        self.telegramFrame.setStyleSheet("")
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
        font.setPointSize(-1)
        self.telegramButton.setFont(font)
        self.telegramButton.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/icons8-telegram-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.telegramButton.setIcon(icon23)
        self.telegramButton.setIconSize(QtCore.QSize(35, 35))
        self.telegramButton.setObjectName("telegramButton")
        self.verticalLayout_18.addWidget(self.telegramButton)
        self.clickerFrame = QtWidgets.QFrame(self.centralwidget)
        self.clickerFrame.setGeometry(QtCore.QRect(10, 143, 581, 561))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.clickerFrame.setFont(font)
        self.clickerFrame.setStyleSheet("")
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("")
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout_3.addWidget(self.nameLabel)
        self.burgerButton = QtWidgets.QPushButton(self.clickerFrame)
        self.burgerButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.burgerButton.sizePolicy().hasHeightForWidth())
        self.burgerButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.burgerButton.setFont(font)
        self.burgerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.burgerButton.setAutoFillBackground(False)
        self.burgerButton.setStyleSheet("")
        self.burgerButton.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/бургер1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.burgerButton.setIcon(self.BurgerIcon)
        self.burgerButton.setIconSize(QtCore.QSize(450, 450))
        self.burgerButton.setFlat(True)
        self.burgerButton.setObjectName("burgerButton")
        self.verticalLayout_3.addWidget(self.burgerButton)
        self.statisticsFrame = QtWidgets.QFrame(self.centralwidget)
        self.statisticsFrame.setGeometry(QtCore.QRect(10, 10, 581, 121))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.countLabel.setFont(font)
        self.countLabel.setStyleSheet("")
        self.countLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countLabel.setObjectName("countLabel")
        self.verticalLayout_2.addWidget(self.countLabel)
        self.helpCountLabel = QtWidgets.QLabel(self.statisticsFrame)
        self.helpCountLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.helpCountLabel.setFont(font)
        self.helpCountLabel.setStyleSheet("")
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.settingsLabel.setFont(font)
        self.settingsLabel.setObjectName("settingsLabel")
        self.verticalLayout_8.addWidget(self.settingsLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setObjectName("volumeLabel")
        self.volumeLabel.setStyleSheet("padding: 20px;")
        self.verticalLayout_9.addWidget(self.volumeLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.muteButton = QtWidgets.QPushButton(self.frame_3)
        self.muteButton.setMinimumSize(QtCore.QSize(150, 60))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/icons8-mute-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.muteButton.setIcon(icon17)
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.statisticsLabel.setFont(font)
        self.statisticsLabel.setObjectName("statisticsLabel")
        self.verticalLayout_11.addWidget(self.statisticsLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
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
        self.exitButton = QtWidgets.QPushButton(self.frame_4)
        self.exitButton.setMinimumSize(QtCore.QSize(150, 60))
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/icons8-close-window-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon21)
        self.exitButton.setIconSize(QtCore.QSize(35, 35))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setStyleSheet('padding: 0 10px;')
        self.verticalLayout_13.addWidget(self.exitButton, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_14.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.settingsWrapper, 0, QtCore.Qt.AlignHCenter)
        self.retranslateUi(BurgerClicker)
        self.statisticsToolBox.setCurrentIndex(0)
        BurgerClicker.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(BurgerClicker)

        self.actions(BurgerClicker)

    def retranslateUi(self, BurgerClicker):
        _translate = QtCore.QCoreApplication.translate
        BurgerClicker.setWindowTitle(_translate("BurgerClicker", "Burger Clicker"))
        self.upgradesButton.setText(_translate("BurgerClicker", "Улучшения"))
        self.helpsButton.setText(_translate("BurgerClicker", "Помощники"))
        self.mainUpgradeName.setText(_translate("BurgerClicker", f"Размер рта X {self.main_count_1}"))
        self.mainUpgradeBuy.setText(_translate("BurgerClicker", f"{self.main_buy_1} бургеров"))
        self.mainUpgradeName_2.setText(_translate("BurgerClicker", f"Мощность челюсти X {self.main_count_2}"))
        self.mainUpgradeBuy_2.setText(_translate("BurgerClicker", f"{self.main_buy_2} бургеров"))
        self.mainUpgradeName_3.setText(_translate("BurgerClicker", f"Объем желудка X {self.main_count_3}"))
        self.mainUpgradeBuy_3.setText(_translate("BurgerClicker", f"{self.main_buy_3} бургеров"))
        self.mainUpgradeName_4.setText(_translate("BurgerClicker", f"Сила кишки X {self.main_count_4}"))
        self.mainUpgradeBuy_4.setText(_translate("BurgerClicker", f"{self.main_buy_4} бургеров"))
        self.mainUpgradeName_5.setText(_translate("BurgerClicker", f"Аппетит X {self.main_count_5}"))
        self.mainUpgradeBuy_5.setText(_translate("BurgerClicker", f"{self.main_buy_5} бургеров"))
        self.mainUpgradeName_6.setText(_translate("BurgerClicker", f"Уровень бургера (ур. {self.main_count_6})"))
        self.mainUpgradeBuy_6.setText(_translate("BurgerClicker", f"{self.main_buy_6} бургеров"))
        self.helpUpgradeName.setText(_translate("BurgerClicker", f"Капризный ребенок X {self.help_count_1}"))
        self.helpUpgradeBuy.setText(_translate("BurgerClicker", f"{self.help_buy_1} бургеров"))
        self.helpUpgradeName_2.setText(_translate("BurgerClicker", f"Бедный студент X {self.help_count_2}"))
        self.helpUpgradeBuy_2.setText(_translate("BurgerClicker", f"{self.help_buy_2} бургеров"))
        self.helpUpgradeName_3.setText(_translate("BurgerClicker", f"Уставший работяга X {self.help_count_3}"))
        self.helpUpgradeBuy_3.setText(_translate("BurgerClicker", f"{self.help_buy_3} бургеров"))
        self.helpUpgradeName_4.setText(_translate("BurgerClicker", f"Любитель поесть X {self.help_count_4}"))
        self.helpUpgradeBuy_4.setText(_translate("BurgerClicker", f"{self.help_buy_4} бургеров"))
        self.helpUpgradeName_5.setText(_translate("BurgerClicker", f"Голодный толстяк X {self.help_count_5}"))
        self.helpUpgradeBuy_5.setText(_translate("BurgerClicker", f"{self.help_buy_5} бургеров"))
        self.helpUpgradeName_6.setText(_translate("BurgerClicker", f"Америкос X {self.help_count_6}"))
        self.helpUpgradeBuy_6.setText(_translate("BurgerClicker", f"{self.help_buy_6} бургеров"))
        self.nameLabel.setText(_translate("BurgerClicker", self.burger_names_list[0]))
        self.countLabel.setText(_translate("BurgerClicker", f"Съедено: {self.burger_count} бургеров"))
        self.helpCountLabel.setText(_translate("BurgerClicker", f"Помощь: {round(self.helps_speed_count, 1)}/сек"))
        self.settingsLabel.setText(_translate("BurgerClicker", "НАСТРОЙКИ"))
        self.volumeLabel.setText(_translate("BurgerClicker", "ЗВУК"))
        self.muteButton.setText(_translate("BurgerClicker", "ВЫКЛЮЧИТЬ"))
        self.statisticsLabel.setText(_translate("BurgerClicker", "СТАТИСТИКА"))
        self.actualCountLabel.setText(_translate("BurgerClicker", f"Актуальное количество съеденных бургеров: {self.burger_count}"))
        self.allCountLabel.setText(_translate("BurgerClicker", f"Общее количество съеденных бургеров {self.allCount}"))
        self.clickPowerLabel.setText(_translate("BurgerClicker", f"Сила клика: {self.click_power}"))
        self.allUpgradesLabel.setText(_translate("BurgerClicker", f"Общее количество улучшений: {self.allUpgrades}"))
        self.allMainUpgradesLabel.setText(_translate("BurgerClicker", f"Количество улучшений клика: {self.allMainUpgrades}"))
        self.gameSessionTimeLabel.setText(_translate("BurgerClicker", f"Время, проведенное в игре: {self.gameSessionTime}"))
        self.allHelpUpgradesLabel.setText(_translate("BurgerClicker", f"Количество улучшений помощников: {self.allHelpUpgrades}"))
        self.statisticsToolBox.setItemText(self.statisticsToolBox.indexOf(self.page), _translate("BurgerClicker", "ОТКРЫТЬ СТАТИСТИКУ"))
        self.statisticsToolBox.setItemText(self.statisticsToolBox.indexOf(self.page_2), _translate("BurgerClicker", "ЗАКРЫТЬ СТАТИСТИКУ"))
        self.returnButton.setText(_translate("BurgerClicker", "ВЕРНУТЬСЯ"))
        self.exitButton.setText(_translate("BurgerClicker", "СОХРАНИТЬ И ВЫЙТИ"))

    def actions(self, BurgerClicker):

        thread = threading.Thread(target=self.auto_click)
        thread.start()

        self.burgerButton.clicked.connect(lambda: self.onclick())
        self.upgradesButton.clicked.connect(lambda: self.open_main_upgrades())
        self.helpsButton.clicked.connect(lambda: self.open_help_upgrades())
        self.settingsMenuButton.clicked.connect(lambda: self.open_or_close_settings())
        self.muteButton.clicked.connect(lambda: self.mute_or_unmute())
        self.returnButton.clicked.connect(lambda: self.open_or_close_settings())
        self.exitButton.clicked.connect(lambda: BurgerClicker.close())
        self.telegramButton.clicked.connect(lambda : self.open_social(self.telegram_url))
        self.githubButton.clicked.connect(lambda : self.open_social(self.github_url))

        self.mainUpgradeBuy.clicked.connect(lambda: self.main_upgrade_1())
        self.mainUpgradeBuy_2.clicked.connect(lambda: self.main_upgrade_2())
        self.mainUpgradeBuy_3.clicked.connect(lambda: self.main_upgrade_3())
        self.mainUpgradeBuy_4.clicked.connect(lambda: self.main_upgrade_4())
        self.mainUpgradeBuy_5.clicked.connect(lambda: self.main_upgrade_5())
        self.mainUpgradeBuy_6.clicked.connect(lambda: self.main_upgrade_6())
        
        self.helpUpgradeBuy.clicked.connect(lambda: self.help_upgrade_1())
        self.helpUpgradeBuy_2.clicked.connect(lambda: self.help_upgrade_2())
        self.helpUpgradeBuy_3.clicked.connect(lambda: self.help_upgrade_3())
        self.helpUpgradeBuy_4.clicked.connect(lambda: self.help_upgrade_4())
        self.helpUpgradeBuy_5.clicked.connect(lambda: self.help_upgrade_5())
        self.helpUpgradeBuy_6.clicked.connect(lambda: self.help_upgrade_6())
        
    def open_or_close_settings(self):
        if self.settings.width() == 0:
            self.settings.setFixedWidth(1037)
        else:
            self.settings.setFixedWidth(0)
        self.upgrade_stats()
        if self.mute == 0: self.settings_sound.play()
    
    def mute_or_unmute(self):
        iconMute = QtGui.QIcon()
        if self.mute == 0:
                self.mute = 1
                iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-volume-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.muteButton.setText("Включить")
        else:
                self.mute = 0
                iconMute.addPixmap(QtGui.QPixmap(":/icons/icons8-mute-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.muteButton.setText("Выключить")
        self.muteButton.setIcon(iconMute)
            
        
    def open_social(self, url):
        webbrowser.open_new_tab(url)
        if self.mute == 0: self.settings_sound.play()

    def update_count(self):
        self.countLabel.setText(f"Съедено: {round(self.burger_count, 1)} бургеров")
        self.helpCountLabel.setText(f"Помощь: {round(self.helps_speed_count, 1)}/сек")

    def onclick(self):
        self.burger_count += self.click_power
        self.allCount += self.click_power
        self.update_count()
        if self.mute == 0: self.click_sound.play()
        
        upgrades = {
                10: [self.mainUpgrade],
                100: [self.mainUpgrade_2, self.helpUpgrade],
                300: [self.mainUpgrade_3],
                1000: [self.mainUpgrade_4, self.helpUpgrade_3],
                2500: [self.mainUpgrade_5],
                200: [self.mainUpgrade_6],
                500: [self.helpUpgrade_2],
                3000: [self.helpUpgrade_4],
                10000: [self.helpUpgrade_5],
                25000: [self.helpUpgrade_6]
        }
        
        for count, upgrades_list in upgrades.items():
            for upgrade in upgrades_list:
                if self.burger_count >= count:
                    upgrade.setEnabled(True)
                    
        self.max_burger()
        
    def max_burger(self):
        if self.main_count_6 == 10:
            self.mainUpgrade_6.setEnabled(False)
            self.mainUpgradeBuy_6.setEnabled(False)
            self.mainUpgradeName_6.setText(f"Уровень бургера (MAX)")
            self.mainUpgradeBuy_6.setText('^_____^')
            
    def open_main_upgrades(self):
        if self.mainUpgradeFrame.width() == 0:
            self.mainUpgradeFrame.setMaximumWidth(21312312)
            self.helpUpgradeFrame.setMaximumWidth(0)
        if self.mute == 0: self.settings_sound.play()
        
    def open_help_upgrades(self):
        if self.helpUpgradeFrame.width() == 0:
            self.helpUpgradeFrame.setMaximumWidth(21312312)
            self.mainUpgradeFrame.setMaximumWidth(0)
        if self.mute == 0: self.settings_sound.play()

    def upgrade_stats(self):
        self.gameSessionTime = round((time.time() - self.startTime))
        self.actualCountLabel.setText(f"Актуальное количество съеденных бургеров: {round(self.burger_count, 1)}")
        self.allCountLabel.setText(f"Общее количество съеденных бургеров {round(self.allCount,1 )}")
        self.clickPowerLabel.setText(f"Сила клика: {round(self.click_power,1 )}")
        self.allUpgradesLabel.setText(f"Общее количество улучшений: {self.allUpgrades}")
        self.allMainUpgradesLabel.setText(f"Количество улучшений клика: {self.allMainUpgrades}")
        self.gameSessionTimeLabel.setText(f"Время, проведенное в игре: {self.gameSessionTime} сек.")
        self.allHelpUpgradesLabel.setText(f"Количество улучшений помощников: {self.allHelpUpgrades}")
    
    def main_upgrade(self, buy_amount, count_variable, name_label, buy_label, power, name):
        if self.burger_count >= buy_amount:
            self.burger_count -= buy_amount
            self.allUpgrades += 1
            self.allMainUpgrades += 1
            self.click_power += power * self.main_count_6
            if self.mute == 0: self.upgrade_sound.play()
            name_label.setText(f"{name} X {count_variable+1}")
            buy_label.setText(f'{round(buy_amount*1.2)} бургеров')
            self.update_count()
    
    def main_upgrade_1(self):
        self.main_upgrade(self.main_buy_1, self.main_count_1, self.mainUpgradeName,
                          self.mainUpgradeBuy, 0.2, 'Размер рта')
        self.main_buy_1 *= 1.2
        self.main_count_1 += 1
        
    
    def main_upgrade_2(self):
        self.main_upgrade(self.main_buy_2, self.main_count_2, self.mainUpgradeName_2,
                          self.mainUpgradeBuy_2, 0.5, 'Мощность челюсти')
        self.main_buy_2 *= 1.2
        self.main_count_2 += 1
    
    def main_upgrade_3(self):
        self.main_upgrade(self.main_buy_3, self.main_count_3, self.mainUpgradeName_3,
                          self.mainUpgradeBuy_3, 1, 'Объем желудка')
        self.main_buy_3 *= 1.2
        self.main_count_3 += 1
    
    def main_upgrade_4(self):
        self.main_upgrade(self.main_buy_4, self.main_count_4, self.mainUpgradeName_4,
                          self.mainUpgradeBuy_4, 3, 'Сила кишки')
        self.main_buy_4 *= 1.2
        self.main_count_4 += 1
    
    def main_upgrade_5(self):
        self.main_upgrade(self.main_buy_5, self.main_count_5, self.mainUpgradeName_5,
                          self.mainUpgradeBuy_5, 10, 'Аппетит')
        self.main_buy_5 *= 1.2
        self.main_count_5 += 1
    
    def  main_upgrade_6(self):
        if self.burger_count >= self.main_buy_6:
            self.burger_count -= self.main_buy_6
            self.main_buy_6 *= 1 + self.main_count_6 / 2.2
            self.allUpgrades += 1
            self.allMainUpgrades += 1
            self.click_power *= 1.5
            self.helps_speed_count *= 1.5
            self.main_count_6 += 1
            if self.mute == 0: self.upgrade_sound.play()
            self.mainUpgradeName_6.setText(f"Уровень бургера (ур. {self.main_count_6})")
            self.nameLabel.setText(self.burger_names_list[self.main_count_6-1])
            self.BurgerIcon = QtGui.QIcon()
            self.BurgerIcon.addPixmap(QtGui.QPixmap(f"images/imgs/бургер{self.main_count_6}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.burgerButton.setIconSize(QtCore.QSize(450, 450))
            self.burgerButton.setIcon(self.BurgerIcon)
            self.mainUpgradeBuy_6.setText(f'{round(self.main_buy_6)} бургеров')
            self.update_count()
            
            self.max_burger()
    
    def help_upgrade(self, buy_amount, count_variable, name_label, buy_label, power, name):
        if self.burger_count >= buy_amount:
            self.burger_count -= buy_amount
            self.allUpgrades += 1
            self.allHelpUpgrades += 1
            self.helps_speed_count += power * self.main_count_6
            if self.mute == 0: self.upgrade_sound.play()
            name_label.setText(f"{name} X {count_variable + 1}")
            buy_label.setText(f'{round(buy_amount * 1.2)} бургеров')
            self.update_count()
    
    def help_upgrade_1(self):
        self.help_upgrade(self.help_buy_1, self.help_count_1, self.helpUpgradeName,
                          self.helpUpgradeBuy, 0.5, 'Капризный ребенок')
        self.help_buy_1 *= 1.2
        self.help_count_1 += 1
    
    def help_upgrade_2(self):
        self.help_upgrade(self.help_buy_2, self.help_count_2, self.helpUpgradeName_2,
                          self.helpUpgradeBuy_2, 2, 'Бедный студент')
        self.help_buy_2 *= 1.2
        self.help_count_2 += 1
    
    def help_upgrade_3(self):
        self.help_upgrade(self.help_buy_3, self.help_count_3, self.helpUpgradeName_3,
                          self.helpUpgradeBuy_3, 5, 'Уставший работяга')
        self.help_buy_3 *= 1.2
        self.help_count_3 += 1
    
    def help_upgrade_4(self):
        self.help_upgrade(self.help_buy_4, self.help_count_4, self.helpUpgradeName_4,
                          self.helpUpgradeBuy_4, 15, 'Любитель поесть')
        self.help_buy_4 *= 1.2
        self.help_count_4 += 1
    
    def help_upgrade_5(self):
        self.help_upgrade(self.help_buy_5, self.help_count_5, self.helpUpgradeName_5,
                          self.helpUpgradeBuy_5, 50,'Голодный толстяк')
        self.help_buy_5 *= 1.2
        self.help_count_5 += 1
    
    def help_upgrade_6(self):
        self.help_upgrade(self.help_buy_6, self.help_count_6, self.helpUpgradeName_6,
                          self.helpUpgradeBuy_6, 250, 'Америкос')
        self.help_buy_6 *= 1.2
        self.help_count_6 += 1
        
    def auto_click(self):
        self.burger_count += self.helps_speed_count
        self.update_count()
        threading.Timer(1.0, self.auto_click).start()
        