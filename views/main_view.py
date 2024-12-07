# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_viewaqwjYn.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QSpinBox, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(747, 595)
        self.actionNew_File = QAction(MainWindow)
        self.actionNew_File.setObjectName(u"actionNew_File")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon = QIcon()
        iconThemeName = u"QIcon::ThemeIcon::ApplicationExit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 705, 440))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)

        self.p_parameters_avrFailRate_profile_value = QTextEdit(self.frame_2)
        self.p_parameters_avrFailRate_profile_value.setObjectName(u"p_parameters_avrFailRate_profile_value")
        self.p_parameters_avrFailRate_profile_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_avrFailRate_profile_value, 7, 1, 1, 1)

        self.p_parameters_pricePerKwh_profile_value = QTextEdit(self.frame_2)
        self.p_parameters_pricePerKwh_profile_value.setObjectName(u"p_parameters_pricePerKwh_profile_value")
        self.p_parameters_pricePerKwh_profile_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_pricePerKwh_profile_value, 6, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_9, 6, 2, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 4)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.p_parameters_desiredReturnTime_value = QTextEdit(self.frame_2)
        self.p_parameters_desiredReturnTime_value.setObjectName(u"p_parameters_desiredReturnTime_value")
        self.p_parameters_desiredReturnTime_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_desiredReturnTime_value, 9, 1, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_13, 9, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.p_parameters_3dprinter_add_profile_pushButton = QPushButton(self.frame_3)
        self.p_parameters_3dprinter_add_profile_pushButton.setObjectName(u"p_parameters_3dprinter_add_profile_pushButton")

        self.horizontalLayout_2.addWidget(self.p_parameters_3dprinter_add_profile_pushButton)

        self.p_parameters_3dprinter_save_profile_pushButton = QPushButton(self.frame_3)
        self.p_parameters_3dprinter_save_profile_pushButton.setObjectName(u"p_parameters_3dprinter_save_profile_pushButton")

        self.horizontalLayout_2.addWidget(self.p_parameters_3dprinter_save_profile_pushButton)

        self.p_parameters_3dprinter_delete_profile_pushButton = QPushButton(self.frame_3)
        self.p_parameters_3dprinter_delete_profile_pushButton.setObjectName(u"p_parameters_3dprinter_delete_profile_pushButton")

        self.horizontalLayout_2.addWidget(self.p_parameters_3dprinter_delete_profile_pushButton)


        self.gridLayout_2.addWidget(self.frame_3, 5, 2, 1, 2)

        self.p_parameters_3dprinter_name_profile_value = QComboBox(self.frame_2)
        self.p_parameters_3dprinter_name_profile_value.setObjectName(u"p_parameters_3dprinter_name_profile_value")
        self.p_parameters_3dprinter_name_profile_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_3dprinter_name_profile_value, 5, 1, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 4)

        self.p_parameters_3dPrinterConsumption_profile_value = QTextEdit(self.frame_2)
        self.p_parameters_3dPrinterConsumption_profile_value.setObjectName(u"p_parameters_3dPrinterConsumption_profile_value")
        self.p_parameters_3dPrinterConsumption_profile_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_3dPrinterConsumption_profile_value, 6, 3, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_14, 7, 2, 1, 1)

        self.p_parameters_3dprinterValue_profile_value = QTextEdit(self.frame_2)
        self.p_parameters_3dprinterValue_profile_value.setObjectName(u"p_parameters_3dprinterValue_profile_value")
        self.p_parameters_3dprinterValue_profile_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_3dprinterValue_profile_value, 7, 3, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_15, 9, 2, 1, 1)

        self.p_parameters_workHoursDay_value = QTextEdit(self.frame_2)
        self.p_parameters_workHoursDay_value.setObjectName(u"p_parameters_workHoursDay_value")
        self.p_parameters_workHoursDay_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_workHoursDay_value, 9, 3, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_16, 10, 0, 1, 1)

        self.p_parameters_workDaysMonth_value = QTextEdit(self.frame_2)
        self.p_parameters_workDaysMonth_value.setObjectName(u"p_parameters_workDaysMonth_value")
        self.p_parameters_workDaysMonth_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_workDaysMonth_value, 10, 1, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_12, 10, 2, 1, 1)

        self.p_parameters_fixedCosts_value = QTextEdit(self.frame_2)
        self.p_parameters_fixedCosts_value.setObjectName(u"p_parameters_fixedCosts_value")
        self.p_parameters_fixedCosts_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_fixedCosts_value, 10, 3, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.p_parameters_length_used_value = QTextEdit(self.frame_2)
        self.p_parameters_length_used_value.setObjectName(u"p_parameters_length_used_value")
        self.p_parameters_length_used_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_length_used_value, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label_4, 2, 2, 1, 1)

        self.p_parameters_filament_price_value = QTextEdit(self.frame_2)
        self.p_parameters_filament_price_value.setObjectName(u"p_parameters_filament_price_value")
        self.p_parameters_filament_price_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_filament_price_value, 1, 3, 1, 1)

        self.p_parameters_estimated_print_time_value = QTextEdit(self.frame_2)
        self.p_parameters_estimated_print_time_value.setObjectName(u"p_parameters_estimated_print_time_value")
        self.p_parameters_estimated_print_time_value.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_estimated_print_time_value, 2, 3, 1, 1)

        self.p_parameters_filament_comboBox = QComboBox(self.frame_2)
        self.p_parameters_filament_comboBox.addItem("")
        self.p_parameters_filament_comboBox.addItem("")
        self.p_parameters_filament_comboBox.setObjectName(u"p_parameters_filament_comboBox")
        self.p_parameters_filament_comboBox.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.p_parameters_filament_comboBox, 1, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 4)


        self.gridLayout_8.addWidget(self.frame_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.parameters_tab, "")
        self.results_tab = QWidget()
        self.results_tab.setObjectName(u"results_tab")
        self.gridLayout_3 = QGridLayout(self.results_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_2 = QScrollArea(self.results_tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 705, 393))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.label_21, 2, 0, 1, 1)

        self.p_results_failure_cost_label = QLabel(self.frame_4)
        self.p_results_failure_cost_label.setObjectName(u"p_results_failure_cost_label")
        self.p_results_failure_cost_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.p_results_failure_cost_label, 1, 3, 1, 1)

        self.p_results_material_cost_label = QLabel(self.frame_4)
        self.p_results_material_cost_label.setObjectName(u"p_results_material_cost_label")
        self.p_results_material_cost_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.p_results_material_cost_label, 1, 1, 1, 1)

        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 40))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 4)

        self.p_results_finishing_cost_label = QLabel(self.frame_4)
        self.p_results_finishing_cost_label.setObjectName(u"p_results_finishing_cost_label")
        self.p_results_finishing_cost_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.p_results_finishing_cost_label, 2, 3, 1, 1)

        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.label_23, 3, 0, 1, 1)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.label_22, 2, 2, 1, 1)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.label_20, 1, 2, 1, 1)

        self.p_results_maitenance_cost_label = QLabel(self.frame_4)
        self.p_results_maitenance_cost_label.setObjectName(u"p_results_maitenance_cost_label")
        self.p_results_maitenance_cost_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.p_results_maitenance_cost_label, 3, 1, 1, 1)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)

        self.p_results_energy_cost_label = QLabel(self.frame_4)
        self.p_results_energy_cost_label.setObjectName(u"p_results_energy_cost_label")
        self.p_results_energy_cost_label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.p_results_energy_cost_label, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_30 = QLabel(self.frame_6)
        self.label_30.setObjectName(u"label_30")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_30.setFont(font1)

        self.gridLayout_7.addWidget(self.label_30, 0, 1, 1, 1)

        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_29.setFont(font2)

        self.gridLayout_7.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_31 = QLabel(self.frame_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.gridLayout_7.addWidget(self.label_31, 1, 0, 1, 1)

        self.label_32 = QLabel(self.frame_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.gridLayout_7.addWidget(self.label_32, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.results_tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.p_results_profit_percentage_value = QSpinBox(self.frame_5)
        self.p_results_profit_percentage_value.setObjectName(u"p_results_profit_percentage_value")
        self.p_results_profit_percentage_value.setMaximum(1000)
        self.p_results_profit_percentage_value.setSingleStep(5)
        self.p_results_profit_percentage_value.setValue(100)

        self.gridLayout_5.addWidget(self.p_results_profit_percentage_value, 0, 1, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 1, 0, 1, 1)

        self.tabWidget.addTab(self.results_tab, "")
        self.history_tab = QWidget()
        self.history_tab.setObjectName(u"history_tab")
        self.tabWidget.addTab(self.history_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.p_main_calculate_results_pushButton = QPushButton(self.frame)
        self.p_main_calculate_results_pushButton.setObjectName(u"p_main_calculate_results_pushButton")

        self.horizontalLayout.addWidget(self.p_main_calculate_results_pushButton)

        self.p_main_clear_parameters_pushButton = QPushButton(self.frame)
        self.p_main_clear_parameters_pushButton.setObjectName(u"p_main_clear_parameters_pushButton")

        self.horizontalLayout.addWidget(self.p_main_clear_parameters_pushButton)

        self.p_main_generate_report_pushButton = QPushButton(self.frame)
        self.p_main_generate_report_pushButton.setObjectName(u"p_main_generate_report_pushButton")

        self.horizontalLayout.addWidget(self.p_main_generate_report_pushButton)

        self.p_main_save_results_pushButton = QPushButton(self.frame)
        self.p_main_save_results_pushButton.setObjectName(u"p_main_save_results_pushButton")

        self.horizontalLayout.addWidget(self.p_main_save_results_pushButton)


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
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"3D Printer", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"3D Printer Consumption (W): ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Printer Costs", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Price per KWh", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Desired return time (months):", None))
        self.p_parameters_3dprinter_add_profile_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Profile", None))
        self.p_parameters_3dprinter_save_profile_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Profile", None))
        self.p_parameters_3dprinter_delete_profile_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Return on 3D Printer investment", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"3D Printer Value:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Hours per day:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Days per Month:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fixed costs per print:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Length used (meters): ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filament Price (per Kg):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Estimated printing time (minutes): ", None))
        self.p_parameters_filament_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"PLA", None))
        self.p_parameters_filament_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ABS", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Filament type:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Filament Costs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameters_tab), QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Energy:", None))
        self.p_results_failure_cost_label.setText("")
        self.p_results_material_cost_label.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Production costs", None))
        self.p_results_finishing_cost_label.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Maitenance:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Finishing (10%):", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Failure:", None))
        self.p_results_maitenance_cost_label.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.p_results_energy_cost_label.setText("")
        self.label_30.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Value for Production:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Value for Sale:", None))
        self.label_32.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Profit percentage:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), QCoreApplication.translate("MainWindow", u"Results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), QCoreApplication.translate("MainWindow", u"History", None))
        self.p_main_calculate_results_pushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate Results", None))
        self.p_main_clear_parameters_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Parameters", None))
        self.p_main_generate_report_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.p_main_save_results_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Results", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_Parameters.setTitle(QCoreApplication.translate("MainWindow", u"&Parameters", None))
        self.menu_Currency.setTitle(QCoreApplication.translate("MainWindow", u"&Currency", None))
    # retranslateUi

