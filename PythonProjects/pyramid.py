#for i in range(1, 6):
#    match(i):
#        case 1:
#            print(i)
#        case 2:
#            print(i,i, sep="")
#        case 3:
#            print(i,i,i, sep="")
#        case 4:
#            print(i,i,i, sep="")
#        case 5:
#            print(i,i,i,i, sep="")

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
