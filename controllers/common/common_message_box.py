from PySide6.QtWidgets import QMessageBox

class SimpleMessages:
    def __init__(self):
        pass

    @staticmethod
    def show_info_message(title, message):
        dlg = QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setText(message)
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK!")
            return True
        else:
            print("Cancel!")
            return False
