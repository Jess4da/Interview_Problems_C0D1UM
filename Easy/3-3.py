def showStar(n):
    print("n = {0}".format(n))
    for i in range(n):
        for j in range(n-1,i,-1):
            print(" ", end="")
        if (i == 0):
            print("*")
            continue
        for j in range(2):
            print("*", end="")
            for k in range((2*i)-1):
                print(" ", end="")
        print("")

n = int(input("Enter n : "))
showStar(n)