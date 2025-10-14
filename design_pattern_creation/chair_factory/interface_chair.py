from abc import ABCMeta, abstractmethod
class IChair():
    
    @staticmethod
    @abstractmethod
    def get_dimensions()-> None :
        #"An abstract interface method"
        return "Please implement this method in subclass"