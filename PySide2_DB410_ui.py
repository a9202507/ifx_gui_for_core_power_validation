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
        MainWindow.resize(733, 851)
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
        self.label_10.setPixmap(QPixmap(u"IFX_LOGO_RGB.jpg"))
        self.label_10.setScaledContents(True)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(190, 10, 511, 71))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_23.setFont(font1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 90, 701, 711))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 320, 351, 221))
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

        self.lineEdit_22 = QLineEdit(self.groupBox_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_3.addWidget(self.lineEdit_22, 3, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBox_3, 4, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)

        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 640, 661, 23))
        self.progressBar.setValue(24)
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 351, 301))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_4.addWidget(self.lineEdit_17, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_4.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_2 = QRadioButton(self.groupBox_6)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox_6)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)


        self.gridLayout_4.addWidget(self.groupBox_6, 7, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_4.addWidget(self.lineEdit_16, 0, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_4.addWidget(self.lineEdit_5, 5, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_4.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_4.addWidget(self.lineEdit_8, 6, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 7, 0, 1, 1)

        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(380, 20, 301, 521))
        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 553, 661, 71))
        self.gridLayout_5 = QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_5 = QPushButton(self.groupBox_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)

        self.gridLayout_5.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)

        self.gridLayout_5.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)

        self.gridLayout_5.addWidget(self.pushButton_8, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 471, 176))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)

        self.gridLayout.addWidget(self.pushButton_6, 4, 2, 1, 1)

        self.lineEdit_28 = QLineEdit(self.groupBox_2)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_28, 1, 0, 1, 3)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)

        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 2)

        self.lineEdit_29 = QLineEdit(self.groupBox_2)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_29, 3, 0, 1, 3)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 200, 473, 174))
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_4 = QCheckBox(self.groupBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_4, 0, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_4)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_5, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox, 3, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_2, 4, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)

        self.gridLayout_2.addWidget(self.pushButton_7, 4, 2, 1, 1)

        self.lineEdit_27 = QLineEdit(self.groupBox_4)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_2.addWidget(self.lineEdit_27, 1, 1, 1, 2)

        self.lineEdit_26 = QLineEdit(self.groupBox_4)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_2.addWidget(self.lineEdit_26, 0, 1, 1, 2)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 2, 1, 1, 2)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(500, 10, 181, 141))
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_9 = QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.groupBox_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.groupBox_5)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_11)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 733, 26))
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
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"LoadSlammer GUI", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Transient-3D", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"duty list(%)", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"10,20,30", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Frequency_list (Khz)", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"10,20,30,100,200,300", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ton duration time(Sec)", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"3D roll up/down enable", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Toff duration time(Sec)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Function Generator setting", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gain mV/A", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"rise time(nSec)", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.groupBox_6.setTitle("")
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Low current(A)", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"765", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"High current(A)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frequency(Khz)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"duct (%)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"fall time(nSec)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.groupBox_7.setTitle("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Clear log", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"abort 3D test", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Start 3D  test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"main", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Equipments setting", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Escope", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Function Generator", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"re-scan equipments", None))
        self.lineEdit_28.setText("")
        self.lineEdit_29.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Misc", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Save as MSO", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Save as PC", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"output filename", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"filename include transinet condition", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"filename include trimstamp", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Save waveform once", None))
        self.lineEdit_27.setText(QCoreApplication.translate("MainWindow", u"C:/temp", None))
        self.lineEdit_26.setText(QCoreApplication.translate("MainWindow", u"C:/temp", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"IFX_DB410_", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"test only", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"pushButton_9", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"pushButton_10", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"pushButton_11", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"setting", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

