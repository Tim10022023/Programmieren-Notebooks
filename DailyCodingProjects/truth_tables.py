def XOR(a, b):
    if a == b:
        return False
    else:
        return True

def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False
    
def OR(a,b):
    if a == 1 or b == 1:
        return True
    else:
        return False

def NOT(a):
    if a == 0:
        return True
    else:
        return False

def NAND(a, b):
    if a == 0 or b == 0:
        return True
    else:
        return False

def NOR(a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True

def XNOR(a,b):
    if a == b:
        return True
    else: 
        return False

print(XOR(1, 1))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(0, 0))
print("")
print(AND(1, 1))
print(AND(1, 0))
print(AND(0, 1))
print(AND(0, 0))
