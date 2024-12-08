"""
Entry point for the 3Dlytic application.
Run this script to start the application.

Usage: $ python main.py
"""
import sys
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController

def load_stylesheet():
    """Load the QSS stylesheet."""
    try:
        with open("resources/styles.qss", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Stylesheet file not found.")
        return ""

def main():
    """
    Main entry point for the 3Dlytic application.

    This function initializes the QApplication, loads the application stylesheet,
    creates the main controller, and starts the application event loop.
    """
    app = QApplication(sys.argv)

    # Load and apply the stylesheet
    stylesheet = load_stylesheet()
    #app.setStyleSheet(stylesheet)

    controller = MainController()
    controller.show()
    app.exec()
    #sys.exit(app.exec())

if __name__ == "__main__":
    main()
