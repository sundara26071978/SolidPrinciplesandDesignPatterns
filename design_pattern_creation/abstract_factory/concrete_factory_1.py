from abstract_factory import IAbstractFactory
from concrete_product_a1 import ConcreteProductA1   
from concrete_product_b1 import ConcreteProductB1

class ConcreteFactory1(IAbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    def create_product_b(self):
        return ConcreteProductB1()
    

