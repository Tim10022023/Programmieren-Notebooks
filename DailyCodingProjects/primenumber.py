def check_number(zahl):
    if zahl < 2:
        return False
    for i in range(2, int(zahl**0.5) + 1):
        if zahl % i == 0:
            return False
    return True

zahl = int(input("Enter a number: "))
if check_number(zahl):
    print(f"{zahl} is prime number.")
else:
    print(f"{zahl} is no prime number.")
