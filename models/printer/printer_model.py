from tinydb import TinyDB, Query

class PrinterData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.db = TinyDB('models/printer/printers_info.json')

    def add_printer(self, printer_info):
        self.db.insert(printer_info)

    def upsert_printer(self, printer_info):
        self.db.upsert(printer_info, Query().name == printer_info["name"])

    def get_printers(self):
        return self.db.all()

    def delete_printer(self, printer_id):
        self.db.remove(Query().id == printer_id)

    def update_printer(self, printer_id, printer_info):
        self.db.update(printer_info, Query().id == printer_id)

    def get_printer_info(self, printer_name):
        return self.db.search(Query().name == printer_name)

    def check_if_printer_exists(self, printer_name):
        if self.db.search(Query().name == printer_name) != []:
            return True
        else:
            return False
