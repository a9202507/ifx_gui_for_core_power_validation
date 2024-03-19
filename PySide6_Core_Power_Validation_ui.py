# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PySide6_Core_Power_Validation_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 860)
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
        self.label_10.setPixmap(QPixmap(u"resource/IFX_LOGO_RGB.jpg"))
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
        self.groupBox_3.setGeometry(QRect(10, 330, 371, 231))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_3.addWidget(self.lineEdit_13, 0, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.groupBox_3)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_3.addWidget(self.lineEdit_21, 2, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_3.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.groupBox_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_3.addWidget(self.lineEdit_22, 3, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBox_3, 4, 1, 1, 1)

        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 640, 661, 23))
        self.progressBar.setValue(24)
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 371, 311))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 4, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 5, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 5, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)

        self.comboBox_8 = QComboBox(self.groupBox)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox_8, 0, 1, 1, 2)

        self.lineEdit_17 = QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_2.addWidget(self.lineEdit_17, 1, 1, 1, 2)

        self.lineEdit_16 = QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_2.addWidget(self.lineEdit_16, 2, 1, 1, 2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 3, 1, 1, 2)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 6, 1, 1, 2)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_2.addWidget(self.lineEdit_8, 7, 1, 1, 2)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout.addWidget(self.label_12)

        self.radioButton_2 = QRadioButton(self.groupBox_6)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox_6)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)


        self.gridLayout_2.addWidget(self.groupBox_6, 8, 0, 1, 3)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 573, 671, 51))
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

        self.groupBox_11 = QGroupBox(self.tab)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(410, 10, 271, 551))
        self.textEdit = QTextEdit(self.groupBox_11)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 20, 251, 521))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 461, 241))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_28 = QLineEdit(self.groupBox_2)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_28, 3, 0, 1, 3)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox_2)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout.addWidget(self.comboBox_6, 0, 1, 1, 2)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)

        self.gridLayout.addWidget(self.pushButton_6, 8, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.lineEdit_29 = QLineEdit(self.groupBox_2)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_29, 7, 0, 1, 3)

        self.label_22 = QLabel(self.groupBox_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 2)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 5, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 5, 1, 1, 2)

        self.comboBox_7 = QComboBox(self.groupBox_2)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout.addWidget(self.comboBox_7, 4, 1, 1, 2)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 260, 461, 241))
        self.checkBox_4 = QCheckBox(self.groupBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setGeometry(QRect(10, 110, 201, 31))
        self.checkBox_4.setChecked(True)
        self.checkBox_5 = QCheckBox(self.groupBox_4)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setGeometry(QRect(10, 140, 201, 31))
        self.checkBox_5.setChecked(True)
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 82, 112, 16))
        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 170, 201, 31))
        self.checkBox_2.setChecked(True)
        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QRect(310, 170, 141, 28))
        self.lineEdit_27 = QLineEdit(self.groupBox_4)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setEnabled(True)
        self.lineEdit_27.setGeometry(QRect(159, 54, 291, 22))
        self.lineEdit_27.setCursorPosition(8)
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_26 = QLineEdit(self.groupBox_4)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(159, 26, 291, 22))
        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(159, 82, 291, 22))
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 26, 141, 16))
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 54, 141, 16))
        self.pushButton_11 = QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setGeometry(QRect(310, 130, 141, 28))
        self.checkBox_6 = QCheckBox(self.groupBox_4)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(10, 200, 201, 31))
        self.checkBox_6.setChecked(True)
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(500, 10, 181, 81))
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_9 = QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton_9)

        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(500, 100, 181, 151))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_19 = QLabel(self.groupBox_8)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_2.addWidget(self.label_19)

        self.comboBox_3 = QComboBox(self.groupBox_8)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_2.addWidget(self.comboBox_3)

        self.label_20 = QLabel(self.groupBox_8)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_2.addWidget(self.label_20)

        self.comboBox_4 = QComboBox(self.groupBox_8)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_2.addWidget(self.comboBox_4)

        self.groupBox_9 = QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(500, 260, 181, 91))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_21 = QLabel(self.groupBox_9)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_3.addWidget(self.label_21)

        self.comboBox_5 = QComboBox(self.groupBox_9)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.comboBox_5)

        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(500, 590, 181, 71))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_10 = QPushButton(self.groupBox_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)

        self.verticalLayout_4.addWidget(self.pushButton_10)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 737, 22))
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.comboBox_8)
        QWidget.setTabOrder(self.comboBox_8, self.lineEdit_17)
        QWidget.setTabOrder(self.lineEdit_17, self.lineEdit_16)
        QWidget.setTabOrder(self.lineEdit_16, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.lineEdit_13)
        QWidget.setTabOrder(self.lineEdit_13, self.lineEdit_15)
        QWidget.setTabOrder(self.lineEdit_15, self.lineEdit_21)
        QWidget.setTabOrder(self.lineEdit_21, self.lineEdit_22)
        QWidget.setTabOrder(self.lineEdit_22, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.comboBox_6)
        QWidget.setTabOrder(self.comboBox_6, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.lineEdit_28)
        QWidget.setTabOrder(self.lineEdit_28, self.comboBox_7)
        QWidget.setTabOrder(self.comboBox_7, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.lineEdit_29)
        QWidget.setTabOrder(self.lineEdit_29, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.lineEdit_26)
        QWidget.setTabOrder(self.lineEdit_26, self.lineEdit_27)
        QWidget.setTabOrder(self.lineEdit_27, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.checkBox_4)
        QWidget.setTabOrder(self.checkBox_4, self.checkBox_5)
        QWidget.setTabOrder(self.checkBox_5, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.checkBox_6)
        QWidget.setTabOrder(self.checkBox_6, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.comboBox_5)
        QWidget.setTabOrder(self.comboBox_5, self.pushButton_10)

        self.menubar.addAction(self.menuabout.menuAction())
        self.menuabout.addAction(self.actionLoad_config)
        self.menuabout.addAction(self.actionSave_config)
        self.menuabout.addSeparator()
        self.menuabout.addAction(self.actionAbout_the_GUI)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout_the_GUI.setText(QCoreApplication.translate("MainWindow", u"About the GUI", None))
        self.actionLoad_config.setText(QCoreApplication.translate("MainWindow", u"Load config", None))
        self.actionSave_config.setText(QCoreApplication.translate("MainWindow", u"Save config", None))
        self.label_10.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Infineon GUI for core power validation", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Transient-3D", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"T_on duration time (s)", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"10,20,30", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"T_off duration time (s)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Frequency list (kHz)", None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"10,20,30,100,200,300", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Duty cycle list (%)", None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"3D roll up/down enable", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Function Generator settings", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Load Imp. (Ohm)\n"
"select or enter value", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gain (mV/A)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"High current (A)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Low current (A)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Slew rate (rise) (A/\u00b5s)", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Rise time: xxxx ns  ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Slew rate (fall) (A/\u00b5s)", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Fall time: xxxx ns", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Duty cycle (%)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frequency (kHz)", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"HiZ", None))

        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.groupBox_6.setTitle("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.groupBox_7.setTitle("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Clear log", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Abort 3D test", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Start 3D  test", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Equipment selection", None))
        self.lineEdit_28.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Scope type", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"re-scan equipment", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Function generator type", None))
        self.lineEdit_29.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Scope address", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Function generator address", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Misc", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Save screenshots on scope", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Save screenshots on PC", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Screenshot prefix", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Add timestamp to filename", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Test Screenshot", None))
        self.lineEdit_27.setText(QCoreApplication.translate("MainWindow", u"./report", None))
        self.lineEdit_26.setText(QCoreApplication.translate("MainWindow", u"C:/temp", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"IFX_DB410_", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output folder in scope", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Output folder in PC", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Set output folder (PC)", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Automatically create 3D plot", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Report", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Create 3D report", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Scope channel settings", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"V_out channel", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"I_out channel", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Funct. gen. channel settings", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Debug Mode", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Toggle Debug Mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

