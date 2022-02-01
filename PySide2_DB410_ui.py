# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PySide2_DB410_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(723, 900)
        self.actionAbout_the_GUI = QAction(MainWindow)
        self.actionAbout_the_GUI.setObjectName(u"actionAbout_the_GUI")
        self.actionLoad_config = QAction(MainWindow)
        self.actionLoad_config.setObjectName(u"actionLoad_config")
        self.actionSave_config = QAction(MainWindow)
        self.actionSave_config.setObjectName(u"actionSave_config")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 151, 71))
        font = QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setPixmap(QPixmap(u"../../../../Users/Echen3/.designer/VR14_PyGUI/Gen5_VR14-beta/IFX_LOGO_RGB.jpg"))
        self.label_10.setScaledContents(True)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(170, 10, 311, 61))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_23.setFont(font1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 90, 701, 741))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 390, 351, 221))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_3.addWidget(self.lineEdit_13, 0, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_3.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.groupBox_3)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_3.addWidget(self.lineEdit_21, 2, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.groupBox_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_3.addWidget(self.lineEdit_22, 3, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBox_3, 4, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QRect(20, 640, 121, 31))
        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 680, 661, 23))
        self.progressBar.setValue(24)
        self.pushButton_8 = QPushButton(self.tab)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QRect(380, 640, 301, 31))
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 351, 371))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_4.addWidget(self.lineEdit_16, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_4.addWidget(self.lineEdit_17, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_4.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_4.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_4.addWidget(self.lineEdit_5, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 6, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_4.addWidget(self.lineEdit_8, 6, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 7, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_4.addWidget(self.comboBox_3, 7, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)

        self.gridLayout_4.addWidget(self.pushButton_2, 8, 0, 1, 2)

        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(380, 40, 301, 571))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 461, 141))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)

        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 2)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 489, 461, 181))
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_2, 3, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)

        self.gridLayout_2.addWidget(self.pushButton_7, 3, 2, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_26 = QLineEdit(self.groupBox_4)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_2.addWidget(self.lineEdit_26, 0, 1, 1, 2)

        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 1, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 723, 25))
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuabout.menuAction())
        self.menuabout.addAction(self.actionLoad_config)
        self.menuabout.addAction(self.actionSave_config)
        self.menuabout.addSeparator()
        self.menuabout.addAction(self.actionAbout_the_GUI)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout_the_GUI.setText(QCoreApplication.translate("MainWindow", u"About the GUI", None))
        self.actionLoad_config.setText(QCoreApplication.translate("MainWindow", u"Load config", None))
        self.actionSave_config.setText(QCoreApplication.translate("MainWindow", u"Save config", None))
        self.label_10.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"DB410 engineering GUI", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Transient-3D", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"duty list(%)", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"10,20,30", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Frequency_list (Khz)", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"10,20,30,100,200,300", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Delay time(Sec)", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Cooldown time(Sec)", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"3D roll up/down enable", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"abort", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Start ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Function Generator setting", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"High current(A)", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Low current(A)", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gain mV/A", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"rise time(nSec)", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"765", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"fall time(nSec)", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"duct (%)", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frequency(Khz)", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"On/Off", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"off", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"on", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"send command to function generator one time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"main", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"equipments setting", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Escope ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Function Generator", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"re-flash", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Misc", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"filename include trimstamp", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Send a command", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"filename include transinet condition", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"output filename", None))
        self.lineEdit_26.setText(QCoreApplication.translate("MainWindow", u"C:/temp", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Save as MSO:", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"IFX_DB410_", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"setting", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

