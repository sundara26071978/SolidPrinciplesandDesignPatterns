from prototype import Prototype
import copy
class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self._value = value

    def clone(self):
        #return copy.deepcopy(self)
        return ConcretePrototype1(self._value)

    def __str__(self):
        return f"(value={self._value})"
    


if __name__ == "__main__":
    prototype1 = ConcretePrototype1(10)
    clone1 = prototype1.clone()
    # clone1._value = 2032
    print(f"Original: {prototype1}")
    print(f"Clone: {clone1}")