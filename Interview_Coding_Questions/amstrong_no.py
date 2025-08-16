num = 371
temp = num
sum = 0
while temp :
    remainder = temp % 10
    sum += remainder ** len(str(num))
    temp //= 10

if sum == num :
    print(f"{num} is a armstrong number.") 
else:
    print(f"{num} is a not armstrong number.") 

