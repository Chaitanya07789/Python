def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = i * fac
    return fac

print(factorial(4))