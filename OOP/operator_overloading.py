class Demo:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other): # + operator overloading
        return Demo(self.x + other.x , self.y + other.y)
    

    # without this method o/p will be <__main__.Demo object at 0x0000021AFBA1BE50>
    def __str__(self): 
        return f"({self.x}, {self.y})"
    

obj1 = Demo(2,3)
obj2 = Demo(4,5)

print( obj1 + obj2 ) # print method calls __str__ , if written in class



