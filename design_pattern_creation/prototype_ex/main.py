from concrete_prototype_1 import ConcretePrototype1
from concrete_prototype_2 import ConcretePrototype2 

def main():
    print("Prototype Pattern Example")
    print("-------------------------")
    print()
    cp1 = ConcretePrototype1("cp1 value")
    cp2 = ConcretePrototype2("cp2 value")
    clone1 = cp1.clone()
    clone2 = cp2.clone()

    # clone1._value = 2032
    # print(f"Original: {prototype1}")
    # print(f"Clone: {clone1}")
    print("cp1:", cp1,", hash", hash(cp1))
    print("cp2:", cp2,", hash", hash(cp2))
    print("clone1:", clone1,", hash", hash(clone1))
    print("clone2:", clone2,", hash", hash(clone2))

if __name__ == "__main__":
    main()