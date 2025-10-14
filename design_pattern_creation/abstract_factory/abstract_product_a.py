from abc import ABC, abstractmethod

class IAbstractProductA(ABC):
    @abstractmethod
    def build_product_a(self):
        pass