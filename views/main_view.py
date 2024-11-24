# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(747, 595)
        self.actionNew_File = QAction(MainWindow)
        self.actionNew_File.setObjectName(u"actionNew_File")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.actionExit.setIcon(icon)
        self.actionBRL = QAction(MainWindow)
        self.actionBRL.setObjectName(u"actionBRL")
        self.actionUSD = QAction(MainWindow)
        self.actionUSD.setObjectName(u"actionUSD")
        self.actionFilament = QAction(MainWindow)
        self.actionFilament.setObjectName(u"actionFilament")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.parameters_tab = QWidget()
        self.parameters_tab.setObjectName(u"parameters_tab")
        self.gridLayout = QGridLayout(self.parameters_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.parameters_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 705, 409))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textEdit_7 = QTextEdit(self.frame_2)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setEnabled(False)
        self.textEdit_7.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.textEdit_7, 7, 3, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.frame_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.textEdit_3, 1, 3, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)

        self.textEdit_6 = QTextEdit(self.frame_2)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.textEdit_6, 7, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.textEdit_2, 3, 1, 1, 1)

        self.textEdit_4 = QTextEdit(self.frame_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.textEdit_4, 6, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_9, 6, 2, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_12, 7, 2, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 4)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.textEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_2.addWidget(self.pushButton_6)


        self.gridLayout_2.addWidget(self.frame_3, 5, 2, 1, 2)

        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.comboBox_2, 5, 1, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 4)

        self.textEdit_5 = QTextEdit(self.frame_2)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.textEdit_5, 6, 3, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.parameters_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.tabWidget.addTab(self.parameters_tab, "")
        self.results_tab = QWidget()
        self.results_tab.setObjectName(u"results_tab")
        self.tabWidget.addTab(self.results_tab, "")
        self.history_tab = QWidget()
        self.history_tab.setObjectName(u"history_tab")
        self.tabWidget.addTab(self.history_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menu_Parameters = QMenu(self.menubar)
        self.menu_Parameters.setObjectName(u"menu_Parameters")
        self.menu_Currency = QMenu(self.menu_Parameters)
        self.menu_Currency.setObjectName(u"menu_Currency")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Parameters.menuAction())
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionExit)
        self.menu_Parameters.addAction(self.menu_Currency.menuAction())
        self.menu_Currency.addAction(self.actionBRL)
        self.menu_Currency.addAction(self.actionUSD)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_File.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.actionBRL.setText(QCoreApplication.translate("MainWindow", u"BRL (R$)", None))
        self.actionUSD.setText(QCoreApplication.translate("MainWindow", u"USD ($)", None))
        self.actionFilament.setText(QCoreApplication.translate("MainWindow", u"Filament", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Average failure rate (%)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filament Price:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"3D Printer", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"3D Printer Consumption (W): ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Hourly depreciation:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Production Costs", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Price per KWh", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Estimated printing time (minutes): ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"PLA", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ABS", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Nylon", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"PETG", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"ASA", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Filament type:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Add Profile", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Delete Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Return on investment costs", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Filament Costs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Length used (meters): ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Clear Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameters_tab), QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), QCoreApplication.translate("MainWindow", u"Results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), QCoreApplication.translate("MainWindow", u"History", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate Results", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save Results", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_Parameters.setTitle(QCoreApplication.translate("MainWindow", u"&Parameters", None))
        self.menu_Currency.setTitle(QCoreApplication.translate("MainWindow", u"&Currency", None))
    # retranslateUi

