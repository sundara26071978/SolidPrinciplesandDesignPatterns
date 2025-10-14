from abstract_product_a import IAbstractProductA

class ConcreteProductA1(IAbstractProductA):
    def build_product_a(self):
        return "Product A1 built"