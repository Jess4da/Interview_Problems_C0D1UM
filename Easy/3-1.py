def showStar(n):
    print("n = {0}".format(n))
    for i in range(n):
        for j in range(i+1):
            print("*", end = "")
        print("")

n = int(input("Enter n : "))
showStar(n)