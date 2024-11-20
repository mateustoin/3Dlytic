class ExampleModel:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        """Add a item to the data list."""
        self.data.append(item)

    def get_data(self):
        """Return all items in the data list."""
        return self.data

    def clear_data(self):
        """Clear all stored data."""
        self.data.clear()