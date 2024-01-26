from abc import ABC, abstractmethod

class ConfigImpl(ABC):
    @abstractmethod
    def write(self, data, file):
        pass
    
    @abstractmethod
    def read(self, file):
        pass
