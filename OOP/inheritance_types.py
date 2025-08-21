# single inhertance

# class Animal:
#     def speak(self):
#         print("Animal can make a sound.")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks.")

# d = Dog()
# d.speak()
# d.bark()


# multilevel inheritance

# class Animal:
#     def speak(self):
#         print("Anime can make sound.")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks.")

# class Puppy(Dog):
#     def play(self):
#         print("Puppy loves to play")
        

# p = Puppy()
# p.speak()
# p.bark()
# p.play()


# multiple inhertance

# class Father:
#     def skill(self):
#         print("Father : Gardening")

# class Mother:
#     def skill(self):
#         print("Mother : Cooking")

# class Child(Father,Mother):
#     def skills(self):
#         Father.skill(self)
#         Mother.skill(self)
#         print("Child : Programming")

# c = Child()
# c.skills()

# hierarchical inhertance

# class Vehicle:
#     def info(self):
#         print("This is a vehicle.")

# class Car(Vehicle):
#     def car_info(self):
#         print("This is car.")

# class Bike(Vehicle):
#     def bike_info(self):
#         print("This is a bike.")


# car = Car()
# car.info()
# car.car_info()

# bike = Bike()
# bike.info()
# bike.bike_info()

# hybrid inhertance  (Multiple + Hierarchical)

# class A:
#     def method_A(self):
#         print("this is class A")

# class B(A):
#     def method_B(self):
#         print("this is class B")

# class C(A):
#     def method_C(self):
#         print("this is class C")

# class D(B,C):
#     def method_D(self):
#         print("this is class D")

# d = D()
# d.method_A()
# d.method_B()
# d.method_C()
# d.method_D()

# # Python resolves ambiguity using MRO (Method Resolution Order).
# print(D.mro())

# o/p: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Explanation of the MRO Order:
# D → Python starts with the class you’re using (D).
# B → Since D inherits from B first (look at class D(B, C)), Python looks into B.
# C → If method not found in B, then Python moves to C.
# A → Both B and C inherit from A. Instead of searching A twice, Python includes it only once (to avoid ambiguity).
# object → The ultimate parent class in Python (all classes in Python 3 inherit from object).

# Why Not [D, B, A, C, object]?
# You might wonder: why didn’t Python check A right after B?
# This is because of the C3 linearization rule:
# It ensures consistent ordering.
# A child class (D) must appear before its parents (B, C, A).
# It keeps the order of base classes as specified in the class definition (class D(B, C) → B comes before C).

# example 1:

# class A:
#     def method_A(self):
#         print("This is class A")

# class B(A):
#     def method_A(self):   # override method_A from A
#         print("This is class B's method_A")

# class C(A):
#     def method_A(self):   # override method_A from A
#         print("This is class C's method_A")

# class D(B, C):   # Multiple inheritance
#     def method_D(self):
#         print("This is class D")

# print(D.mro())

# d = D()
# d.method_A()   # Which one will be called?

# o/p : This is class B's method_A

# example 2:

# class A:
#     def __init__(self, name):
#         self.name = name
#         print(f"A initialized with name = {self.name}")

#     def method_A(self):
#         print(f"Hello from A, name = {self.name}")


# class B(A):
#     def __init__(self, name, age):
#         super().__init__(name)  
#         self.age = age
#         print(f"B initialized with age = {self.age}")

#     def method_B(self):
#         print(f"Hello from B, name = {self.name}, age = {self.age}")


# class C(A):
#     def __init__(self, name, salary):
#         super().__init__(name)   
#         self.salary = salary
#         print(f"C initialized with salary = {self.salary}")

#     def method_C(self):
#         print(f"Hello from C, name = {self.name}, salary = {self.salary}")


# class D(B, C):
#     def __init__(self, name, age, salary, city):
#         super().__init__(name, age)
#         self.salary = salary
#         self.city = city
#         print(f"D initialized with city = {self.city}")

#     def method_D(self):
#         print(f"Hello from D, name = {self.name}, age = {self.age}, salary = {self.salary}, city = {self.city}")


# d = D("Chaitanya", 25, 50000, "Pune")

# print(D.mro())
# d.method_A()

# o/p : TypeError: C.__init__() missing 1 required positional argument: 'salary'

#  classic multiple inheritance + super() problem:

# When super().__init__() is called inside B, Python doesn’t jump directly to A.
# It goes to the next class in MRO after B → C.
# But your C.__init__ expects (name, salary), and B only forwarded (name), so Python complains.

# it can be solved using **kwargs 

class A:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)   # Pass remaining args forward
        self.name = name
        print(f"A initialized with name = {self.name}")

    def method_A(self):
        print(f"Hello from A, name = {self.name}")


class B(A):
    def __init__(self, age, **kwargs):
        super().__init__(**kwargs)   # Pass remaining args forward
        self.age = age
        print(f"B initialized with age = {self.age}")

    def method_B(self):
        print(f"Hello from B, age = {self.age}, name = {self.name}")


class C(A):
    def __init__(self, salary, **kwargs):
        super().__init__(**kwargs)   # Pass remaining args forward
        self.salary = salary
        print(f"C initialized with salary = {self.salary}")

    def method_C(self):
        print(f"Hello from C, salary = {self.salary}, name = {self.name}")


class D(B, C):
    def __init__(self, city, **kwargs):
        super().__init__(**kwargs)   # Calls next in MRO (B → C → A)
        self.city = city
        print(f"D initialized with city = {self.city}")

    def method_D(self):
        print(f"Hello from D, name = {self.name}, age = {self.age}, salary = {self.salary}, city = {self.city}")


# Now call
d = D(name="Chaitanya", age=25, salary=50000, city="Pune")

print(D.mro())
d.method_A()
# d.method_B()
# d.method_C()
# d.method_D()

# o/p: like MRO ->  D → B → C → A
# A initialized with name = Chaitanya
# C initialized with salary = 50000
# B initialized with age = 25
# D initialized with city = Pune
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# Hello from A, name = Chaitanya
