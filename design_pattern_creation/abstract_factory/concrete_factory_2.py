from abstract_factory import IAbstractFactory
from concrete_product_a2 import ConcreteProductA2
from concrete_product_b2 import ConcreteProductB2

class ConcreteFactory2(IAbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    def create_product_b(self):
        return ConcreteProductB2()