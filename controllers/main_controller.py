from PySide6.QtWidgets import QMainWindow
from views.main_view import Ui_MainWindow
from models.example_model import ExampleModel
from config import settings as config
from controllers.printer.printer_controller import PrinterController

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Create an instance of the model
        self.model = ExampleModel()
        self.printer_controller = PrinterController(self.ui)

        # Title configurations
        self.setWindowTitle(f"{config.APP_NAME} v{config.VERSION}")

