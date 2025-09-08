# Write a Python function that takes a list of integers and 
# returns a new list containing only the prime numbers from it.

def prime_generator(numbers):
    for num in numbers:
        if num > 1 :
            for i in range(2,int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                yield num # generator

def get_prime(numbers):
    return [p for p in prime_generator(numbers)] # list comprehension
    # without list comprehension
    # primes = []
    # for p in prime_generator(nums):
    #     primes.append(p)
    # return primes

nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Prime No : " ,get_prime(nums))
