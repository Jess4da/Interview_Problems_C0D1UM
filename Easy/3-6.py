def showChar(n):
    print("n = {0}".format(n))
    
    for i in range(n-1):
        for j in range(i,n-1):
            print("A",end="")
        if (i == 0):
            print("+",end="")
        else:
            print("+",end="")
            for j in range((2*i)-1):
                print("E",end="")
            print("+",end="")
        for j in range(i,n-1):
            print("B",end="")
        print("")
    for i in range(n-1,-1,-1):
        for j in range(i,n-1):
            print("A",end="")
        if (i == 0):
            print("+",end="")
        else:
            print("+",end="")
            for j in range((2*i)-1):
                print("E",end="")
            print("+",end="")
        for j in range(i,n-1):
            print("B",end="")
        print("")

n = int(input("Enter n : "))
showChar(n)
