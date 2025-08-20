# Parent class or base class
class Animal:
    def speak(self):
        print("Animal can make sound.")

# Child class or derived class 
class Dog(Animal):
    def bark(self):
        print("Dog barks.")

d = Dog()
d.speak()
d.bark()
