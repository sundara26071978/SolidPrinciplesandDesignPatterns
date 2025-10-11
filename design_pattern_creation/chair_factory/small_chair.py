from interface_chair import IChair

class SmallChair(IChair):
    """Concrete implementation of IChair interface for small chairs."""
    def __init__(self):
        self.height = 40
        self.width = 40
        self.depth = 40
    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}
    
