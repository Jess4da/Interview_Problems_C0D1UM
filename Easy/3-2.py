def showStar(n):
    print("n = {0}".format(n))
    for i in range(n,0,-1):
        for j in range(i-1):
            print(" ", end="")
        for j in range(i,n+1):
            print("*", end="")
        print("")

n = int(input("Enter n : "))
showStar(n)