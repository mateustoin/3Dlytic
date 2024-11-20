from PySide6.QtWidgets import QMainWindow
from views.main_view import Ui_MainWindow
from models.example_model import ExampleModel
from config import settings as config

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Criar instância do modelo
        self.model = ExampleModel()

        # Conectar botões a métodos
        self.ui.someButton.clicked.connect(self.on_button_click)

        # Outras configurações
        self.setWindowTitle("MyApp - " + config.APP_NAME + " v" + config.VERSION)

    def on_button_click(self):
        """Adiciona o texto ao modelo e exibe os dados na saída."""
        text = self.ui.someTextEdit.toPlainText()
        
        if text.strip():  # Verifica se o texto não está vazio
            self.model.add_data(text)
            self.ui.someTextEdit.clear()  # Limpa o campo de entrada
            print("Texto adicionado:", text)
        else:
            print("Texto vazio, nada adicionado.")

        # Exibir os dados armazenados no modelo
        self.display_data()
        
    def display_data(self):
        """Exibe os dados armazenados no modelo no console."""
        data = self.model.get_data()
        print("Dados armazenados:", data)