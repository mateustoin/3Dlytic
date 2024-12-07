from tinydb import TinyDB, Query

class PrinterData:
    def __init__(self):
        self.db = TinyDB('printers_info.json')
        
        self.name = name
        self.price = price
