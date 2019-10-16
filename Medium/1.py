def showPrime(n):
    numlist = []

    for i in range(2, n+1):
        for j in range(2, int(i**0.5)+1):
            if (i % j) == 0:
                break
        else:
            numlist.append(i)

    print("{0} -> ".format(n), end="")
    for i in range(len(numlist)):
        print("{0} ".format(numlist[i]), end="")
    print("")

n = int(input("Enter n : "))
showPrime(n)