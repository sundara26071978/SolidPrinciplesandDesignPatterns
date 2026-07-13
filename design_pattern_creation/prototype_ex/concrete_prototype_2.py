from prototype import Prototype

class ConcretePrototype2(Prototype):
    def __init__(self, value):
        self._value = value
    def clone(self):
        return ConcretePrototype2(self._value)
    def __str__(self):
        return f"(value={self._value})"
    
if __name__ == "__main__":
    prototype2 = ConcretePrototype2(20)
    clone2 = prototype2.clone()
    print(f"Original: {prototype2}")
    print(f"Clone: {clone2}")
    print(f"Are they the same object? {prototype2 is clone2}")