space = " "
size = 10
for i in range(size):
    if i%2==0:
        print((size-i) * space + 2 * i * "a")
    else:
        print((size-i) * space + 2 * i * "b")
for i in range(8):
    if i%2==0:
        print((size - 1) * space + "xx")
    else:
        print((size-1) * space + "yy")
for i in range(size):
    if i%2==0:
        print((i) * space + 2 * (size-i) * "a")
    else:
        print((i) * space + 2 * (size-i) * "b")   