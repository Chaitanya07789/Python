str = "python"

print(str[2])

# str[2] = "d"  TypeError: 'str' object does not support item assignment
# strings are immutable

str1 = "python"

print(id(str), id(str1))
# both points to same memory address
