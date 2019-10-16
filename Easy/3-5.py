def showStar(n):
    print("n = {0}".format(n))

    for i in range((n//2)):
        for j in range(i,(n//2)):
            print(" ", end="")
        for j in range((2*i)+1):
            print("*",end="")
        print("")
    if (n % 2 == 1 or n == 1):
        for i in range(n):
            print("*", end="")
        print("")
    for i in range((n//2),0,-1):
        for j in range(i,(n//2)+1):
            print(" ", end="")
        for j in range((2*i)-1):
            print("*",end="")
        print("")

n = int(input("Enter n : "))
showStar(n)