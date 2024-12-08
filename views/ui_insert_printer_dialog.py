# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insert_printer_dialogiRqfCc.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGridLayout,
    QLabel, QPlainTextEdit, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(399, 118)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.p_printer_dialog_label = QLabel(Form)
        self.p_printer_dialog_label.setObjectName(u"p_printer_dialog_label")

        self.gridLayout.addWidget(self.p_printer_dialog_label, 0, 0, 1, 1)

        self.p_printer_dialog_input_plainTextEdit = QPlainTextEdit(Form)
        self.p_printer_dialog_input_plainTextEdit.setObjectName(u"p_printer_dialog_input_plainTextEdit")
        self.p_printer_dialog_input_plainTextEdit.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.p_printer_dialog_input_plainTextEdit, 0, 1, 1, 1)

        self.p_printer_dialog_buttonBox = QDialogButtonBox(Form)
        self.p_printer_dialog_buttonBox.setObjectName(u"p_printer_dialog_buttonBox")
        self.p_printer_dialog_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.p_printer_dialog_buttonBox, 1, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.p_printer_dialog_label.setText(QCoreApplication.translate("Form", u"Insert Printer name: ", None))
    # retranslateUi

