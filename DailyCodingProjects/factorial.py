def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

result = factorial(2)

for n in range(5):
    print(factorial(n))