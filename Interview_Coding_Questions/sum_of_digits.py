num = 12345
temp = num
sum = 0
while temp :
    remaider = temp % 10
    sum += remaider
    temp //= 10

print(f"sum of digits of {num} : {sum}")

