num = 23
count = 0
for i in range(2,int((num/2)+1)):
    if num % i == 0:
        count += 1

if count > 0:
    print(f"{num} is a not prime number. ")
else:
     print(f"{num} is a prime number. ")