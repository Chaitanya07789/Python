# Range = 10

# num1 , num2 = 0 , 1
# print(f"Fibonacci Series for given Range {Range}: {num1}, {num2}, " ,end="")
# for i  in range(2,Range):
#     num3 = num1 + num2
#     num1 = num2
#     num2 = num3
#     print(num3,end=", ")



Range = 10
num1, num2 = 0, 1
print(f"fibonacci_series : {num1} {num2} ",end="")
for i in range(2,Range):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3,end=" ")