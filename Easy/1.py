for i in range(1, 101):
    if (i % 15 == 0):
        print("FizzBuzz ", end = "")
    elif (i % 3 == 0):
        print("Fizz ", end = "")
    elif (i % 5 == 0):
        print("Buzz ", end = "")
    else:
        print("{0} ".format(i), end = "")
    if (i % 20 == 0):
        print("")
        