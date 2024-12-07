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

    def on_button_click(self):
        """Add text to the model and display the data in the output."""
        text = self.ui.someTextEdit.toPlainText()
        if text.strip():  # Check if the text is not empty
            self.model.add_data(text)
            self.ui.someTextEdit.clear()  # Clear the input field
            print("Text added:", text)
        else:
            print("Empty text, nothing added.")

        # Display data stored in the model
        self.display_data()

    def display_data(self):
        """Display data stored in the model in the console."""
        data = self.model.get_data()
        print("Stored data:", data)
