# Write a Python program that prints the numbers from 1 to 50, but with the following rules:
# For numbers divisible by 3, print "Fizz" instead of the number.
# For numbers divisible by 5, print "Buzz" instead of the number.
# For numbers divisible by both 3 and 5, print "FizzBuzz".
# For numbers that are prime, print "Prime" instead of the number (even if divisible by 3 or 5).

def prime(num):
    count = 0
    if num == 1:
        return False
    
    for i in range(1,(num//2)+1):
        if num % i ==0:
            count+=1

    if count == 1:
        return True
    
n = 1
while(n <= 50):
    is_prime = prime(n)
    
    if is_prime:
        print("Prime")
    elif n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    n+=1

