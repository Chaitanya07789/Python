# Polymorphism - method overriding and method overloading 
# python does not suppot construct overloading , but it supports operator overloading

class Bird:
    def fly(self):
        return "Some birds can fly"
    
class Parrot(Bird):
    def fly(self): # method overriding
        return "Parrot flies high"
    
class Penguin(Bird):
    def fly(self): # method overriding
        return "Penguin cannot fly"
    
birds = [Bird(), Parrot(), Penguin()]

for b in birds:
    print(b.fly())

