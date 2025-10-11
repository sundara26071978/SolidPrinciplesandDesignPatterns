from interface_chair import IChair

class BigChair(IChair):
    """Concrete implementation of IChair interface for big chairs."""
    def __init__(self):
        self.height = 90
        self.width = 90
        self.depth = 90
    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}    
    
    