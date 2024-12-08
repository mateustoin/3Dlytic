from PySide6.QtWidgets import QDialog
from views.ui_insert_printer_dialog import Ui_Form
from models.printer.printer_model import PrinterData
from controllers.common.common_message_box import SimpleMessages

class PrinterController:
    def __init__(self, ui):
        self.ui = ui
        self.dialog = PrinterDialogWindow()
        self.printer_model = PrinterData()

        # Connect buttons to methods
        self.ui.p_parameters_3dprinter_add_profile_pushButton.clicked.connect(
            self.on_add_printer_button_clicked
        )
        self.dialog.ui.p_printer_dialog_buttonBox.accepted.connect(self.accept_dialog)
        self.dialog.ui.p_printer_dialog_buttonBox.rejected.connect(self.reject_dialog)

        self.ui.p_parameters_3dprinter_save_profile_pushButton.clicked.connect(
            self.on_save_button_click
        )
        #self.ui.p_parameters_3dprinter_delete_profile_pushButton.clicked.connect(
            # self.on_delete_button_click
        # )

    # Show Ui_Form on button click
    def on_add_printer_button_clicked(self):
        print("Button clicked!")
        self.dialog.show()

    def accept_dialog(self):
        print("Dialog accepted!")
        #self.dialog.accept()
        current_printer_name = self.dialog.ui.p_printer_dialog_input_plainTextEdit.toPlainText()
        #self.ui.p_parameters_3dprinter_name_profile_value.addItem(current_printer_name)
        self.dialog.close()
        self.dialog.ui.p_printer_dialog_input_plainTextEdit.clear()

        if (current_printer_name.__len__() == 0):
            SimpleMessages().show_info_message("Error", "Printer must have a name!")
        # TODO: Check if the printer name already exists
        elif self.printer_model.get_printers():
            SimpleMessages().show_info_message("Error", "Printer name already exists!")
        else:
            self.ui.p_parameters_3dprinter_name_profile_value.addItem(current_printer_name)
            self.dialog.close()
            self.dialog.ui.p_printer_dialog_input_plainTextEdit.clear()

    def reject_dialog(self):
        print("Dialog rejected!")
        self.dialog.close()
        self.dialog.ui.p_printer_dialog_input_plainTextEdit.clear()
        #self.dialog.reject()

    def on_save_button_click(self):
        printer_info = self.generate_printer_info()
        self.printer_model.add_printer(printer_info)

    #def on_delete_button_click(self):

    def generate_printer_info(self):
        current_printer_name = self.ui.p_parameters_3dprinter_name_profile_value.currentText()
        price_per_kwh = self.ui.p_parameters_pricePerKwh_profile_value.toPlainText()
        hours_per_day = self.ui.p_parameters_workHoursDay_value.toPlainText()
        days_per_month = self.ui.p_parameters_workDaysMonth_value.toPlainText()
        fixed_costs_per_print = self.ui.p_parameters_fixedCosts_value.toPlainText()
        average_failure_rate = self.ui.p_parameters_avrFailRate_profile_value.toPlainText()
        desired_return_time = self.ui.p_parameters_desiredReturnTime_value.toPlainText()
        printer_consumption = self.ui.p_parameters_3dPrinterConsumption_profile_value.toPlainText()
        printer_value = self.ui.p_parameters_3dprinterValue_profile_value.toPlainText()

        printer_info = {
            "name": current_printer_name,
            "price_per_kwh": price_per_kwh,
            "hours_per_day": hours_per_day,
            "days_per_month": days_per_month,
            "fixed_costs_per_print": fixed_costs_per_print,
            "average_failure_rate": average_failure_rate,
            "desired_return_time": desired_return_time,
            "printer_consumption": printer_consumption,
            "printer_value": printer_value
        }

        print(printer_info)

        return printer_info

class PrinterDialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
