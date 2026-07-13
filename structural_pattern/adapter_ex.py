''' Adapter Design Pattern Example Code '''

# Target Interface
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

# Adaptee
class LegacyPrinter:
    def print_document(self):
        print('Legacy Printer is printing a document.')

# Adapter
class PrinterAdapter(Printer):
    def __init__(self):
        self.legacy_printer = LegacyPrinter()

    def print(self):
        self.legacy_printer.print_document()

# Client Code
def client_code(printer):
    printer.print()

if __name__ == '__main__':
    # Using the Adapter
    adapter = PrinterAdapter()
    client_code(adapter)