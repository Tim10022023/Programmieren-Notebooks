def faktorisierung(n):
    faktoren = []
    teiler = 2

    while teiler * teiler <= n:
        if n % teiler:
            teiler += 1
        else:
            n //= teiler
            faktoren.append(teiler)

    if n > 1:
        faktoren.append(n)

    return faktoren


zahl = 84
ergebnis = faktorisierung(zahl)

print(f"Die Primfaktoren von {zahl} sind: {ergebnis}")
