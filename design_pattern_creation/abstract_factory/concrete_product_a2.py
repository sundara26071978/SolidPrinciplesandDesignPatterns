from abstract_product_a import IAbstractProductA
class ConcreteProductA2(IAbstractProductA):
    def build_product_a(self):
        return "Product A2 built"