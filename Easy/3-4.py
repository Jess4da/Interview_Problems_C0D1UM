def showStar(n):
    print("n = {0}".format(n))

    for i in range((n//2)):
        for j in range(i):
            print(" ", end="")
        print("*", end="")
        for j in range(i*2, n-2):
            print(" ", end="")
        print("*")
        
    if (n % 2 == 1):
        for i in range((n//2)):
            print(" ", end="")
        print("*")

    for i in range((n//2)):
        for j in range((n//2)-i-1):
            print(" ", end="")
        print("*", end="")
        for j in range(((n//2)-i-1)*2, n-2):
            print(" ", end="")
        print("*")

n = int(input("Enter n : "))
showStar(n)