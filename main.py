import sys
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)
    controller = MainController()
    controller.show()
    app.exec()
    #sys.exit(app.exec())

if __name__ == "__main__":
    main()
