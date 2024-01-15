y = [1, 5, 7, 3, 76, 3, 56, 234, 6246, 34]
min = min(y)
max = max(y)
print("Minimum: " + str(min))
print("Maximum: " + str(max))
def remove_duplicates():
    return set(y)
a = remove_duplicates()
for x in a:
    print (x, end=" ")
