from concrete_factory_1 import ConcreteFactory1
from concrete_factory_2 import ConcreteFactory2

def create_products(concrete_factory):
    
    product_a = concrete_factory.create_product_a()
    product_b = concrete_factory.create_product_b()
    print(product_a.build_product_a())
    print(product_b.build_product_b())

def main():
    print("Client: Testing client code with the first factory type:")
    create_products(ConcreteFactory1())
    print("\n")
    print("Client: Testing the same client code with the second factory type:")
    create_products(ConcreteFactory2())

if __name__ == "__main__":
    main()