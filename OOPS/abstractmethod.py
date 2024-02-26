from abc import ABC, abstractmethod 
class Sample(ABC):
    @abstractmethod
    def add(self,a, b):
        return a+b
    def sub(self,a, b):
        return a-b
    
class Test(Sample):
    def add(self,a, b):
        return super().add(a,b)
    
obj =  Test()