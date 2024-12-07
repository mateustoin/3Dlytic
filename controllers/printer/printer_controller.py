from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from views.ui_insert_printer_dialog import Ui_Form

class PrinterController:
    def __init__(self, ui):
        self.ui = ui
        self.dialog = PrinterDialogWindow()
        # Connect buttons to methods
        self.ui.p_parameters_3dprinter_add_profile_pushButton.clicked.connect(self.on_add_printer_button_clicked)
        self.dialog.ui.p_printer_dialog_buttonBox.accepted.connect(self.accept_dialog)
        self.dialog.ui.p_printer_dialog_buttonBox.rejected.connect(self.reject_dialog)

    # Show Ui_Form on button click
    def on_add_printer_button_clicked(self):
        print("Button clicked!")
        self.dialog.show()

    def accept_dialog(self):
        print("Dialog accepted!")
        #self.dialog.accept()
        current_printer_name = self.dialog.ui.p_printer_dialog_input_plainTextEdit.toPlainText()
        self.ui.p_parameters_3dprinter_name_profile_value.addItem(current_printer_name)
        self.dialog.close()
        self.dialog.ui.p_printer_dialog_input_plainTextEdit.clear()

    def reject_dialog(self):
        print("Dialog rejected!")
        self.dialog.close()
        self.dialog.ui.p_printer_dialog_input_plainTextEdit.clear()
        #self.dialog.reject()

class PrinterDialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
