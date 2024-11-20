class ExampleModel:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        """Adiciona um item à lista de dados."""
        self.data.append(item)

    def get_data(self):
        """Retorna todos os itens na lista de dados."""
        return self.data

    def clear_data(self):
        """Limpa todos os dados armazenados."""
        self.data.clear()