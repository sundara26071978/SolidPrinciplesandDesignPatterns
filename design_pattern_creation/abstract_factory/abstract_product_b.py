from abc import ABC, abstractmethod

class IAbstractProductB(ABC):
    @abstractmethod
    def build_product_b(self):
        pass
