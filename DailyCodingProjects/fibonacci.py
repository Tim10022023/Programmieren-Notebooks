def fibonacci_of(n):
    if n<=1:
        return n
    return fibonacci_of(n-1) + fibonacci_of(n-2)

result = fibonacci_of(2)

for n in range(15):
    print(fibonacci_of(n))