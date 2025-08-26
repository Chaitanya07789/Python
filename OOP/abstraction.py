from abc import ABC , abstractmethod

class Base(ABC): # a class which inherites from ABC called abstract class

    def method1(self):
        print("This normal instance method.")

    @abstractmethod
    def method2(self):
        pass # this is abstract method    

class Derived(Base):
    
    def method2(self): # if not defined ,it gives error
        print("this is an abstract methods that need to to defined in child class which inherites abstract class")

# b = Base()  ## abstract class cannot be instantiated
# b.method1()

d = Derived()
d.method2()