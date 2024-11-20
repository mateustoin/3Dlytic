import sys
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController

def load_stylesheet():
    """Load the QSS stylesheet."""
    try:
        with open("resources/styles.qss", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Stylesheet file not found.")
        return ""

def main():
    app = QApplication(sys.argv)
    
    # Load and apply the stylesheet
    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    controller = MainController()
    controller.show()
    app.exec()
    #sys.exit(app.exec())

if __name__ == "__main__":
    main()
