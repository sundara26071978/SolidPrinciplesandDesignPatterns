from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory:
    """Factory class to create chair objects based on size."""
    @staticmethod
    def create_chair(size):
        if size == "small":
            return SmallChair()
        elif size == "medium":
            return MediumChair()
        elif size == "big":
            return BigChair()
        else:
            return None
