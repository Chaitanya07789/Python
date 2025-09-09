class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def __eq__(self, other): # operator overloaded is ==
        return self.area() == other.area()
    
    def __lt__(self,other): # operator overloaded is <
        return self.area() < other.area()
    
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width}, area={self.area()})"
    

r1 = Rectangle(4,5)
r2 = Rectangle(2,10)
r3 = Rectangle(3,4)

print(r1)
print(r2)
print(r3)

print(r1 == r2)
print(r1 < r3)
print(r3 < r1)