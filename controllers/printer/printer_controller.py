from PySide6.QtWidgets import QDialog
from views.ui_insert_printer_dialog import Ui_Form
from models.printer.printer_model import PrinterData
from controllers.common.common_message_box import SimpleMessages

class PrinterController:
    def __init__(self, ui):
        self.ui = ui
        self.dialog = PrinterDialogWindow()
        self.printer_model = PrinterData()
        self.current_printer_profile_name_selected = ""

        self.update_printer_profile_list()

        # Connections to methods
        # Buttons
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
        
        # Events
        self.ui.p_parameters_3dprinter_name_profile_value.currentTextChanged.connect(
            self.update_printer_profile_ui_information
        )

    # Show Ui_Form on button click
    def on_add_printer_button_clicked(self):
        print("Button clicked!")
        self.dialog.show()

    def accept_dialog(self):
        print("Dialog accepted!")
        #self.dialog.accept()
        current_printer_name = self.dialog.ui.p_printer_dialog_input_plainTextEdit.toPlainText()
        printers_list = [self.ui.p_parameters_3dprinter_name_profile_value.itemText(i) 
                         for i in range(self.ui.p_parameters_3dprinter_name_profile_value.count())]

        if (current_printer_name.__len__() == 0):
            SimpleMessages().show_info_message("Error", "Printer must have a name!")
        elif current_printer_name in printers_list:
            SimpleMessages().show_info_message("Error", "Printer name already exists!")
        elif self.printer_model.check_if_printer_exists(current_printer_name):
            SimpleMessages().show_info_message("Error", "Printer name already exists on the database!")
        else:
            self.ui.p_parameters_3dprinter_name_profile_value.addItem(current_printer_name)
            self.clean_ui_information()
            #self.ui.p_parameters_3dprinter_name_profile_value.setCurrentIndex(self.ui.p_parameters_3dprinter_name_profile_value.count() - 1)
            current_profile_added = self.generate_printer_info()
            self.printer_model.add_printer(current_profile_added)
            self.current_printer_profile_name_selected = current_printer_name
            self.update_printer_profile_ui_information()

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

        return printer_info

    def update_printer_profile_list(self):
        self.ui.p_parameters_3dprinter_name_profile_value.clear()
        printer_list = self.printer_model.get_printers()
        for printer in printer_list:
            self.ui.p_parameters_3dprinter_name_profile_value.addItem(printer["name"])

        if printer_list.__len__() > 0:
            self.update_printer_profile_ui_information()

    def update_printer_profile_ui_information(self):
        printer_info = self.printer_model.get_printer_info(self.ui.p_parameters_3dprinter_name_profile_value.currentText())
        print(printer_info)
        self.ui.p_parameters_pricePerKwh_profile_value.setPlainText(printer_info[0]["price_per_kwh"])
        self.ui.p_parameters_workHoursDay_value.setPlainText(printer_info[0]["hours_per_day"])
        self.ui.p_parameters_workDaysMonth_value.setPlainText(printer_info[0]["days_per_month"])
        self.ui.p_parameters_fixedCosts_value.setPlainText(printer_info[0]["fixed_costs_per_print"])
        self.ui.p_parameters_avrFailRate_profile_value.setPlainText(printer_info[0]["average_failure_rate"])
        self.ui.p_parameters_desiredReturnTime_value.setPlainText(printer_info[0]["desired_return_time"])
        self.ui.p_parameters_3dPrinterConsumption_profile_value.setPlainText(printer_info[0]["printer_consumption"])
        self.ui.p_parameters_3dprinterValue_profile_value.setPlainText(printer_info[0]["printer_value"])

    def clean_ui_information(self):
        self.ui.p_parameters_pricePerKwh_profile_value.setPlainText("")
        self.ui.p_parameters_workHoursDay_value.setPlainText("")
        self.ui.p_parameters_workDaysMonth_value.setPlainText("")
        self.ui.p_parameters_fixedCosts_value.setPlainText("")
        self.ui.p_parameters_avrFailRate_profile_value.setPlainText("")
        self.ui.p_parameters_desiredReturnTime_value.setPlainText("")
        self.ui.p_parameters_3dPrinterConsumption_profile_value.setPlainText("")
        self.ui.p_parameters_3dprinterValue_profile_value.setPlainText("")

class PrinterDialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
