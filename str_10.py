str = "python is user friendly language"
list = str.split(" ")  # returns list
list1 = str.partition(" ") # returns tuple
print(list)
print(list1)

# o/p:
# ['python', 'is', 'user', 'friendly', 'language']
# ('python', ' ', 'is user friendly language')