def isLeapYear(year):
    if (year % 400 == 0):
        return "false"
    else:
        if (year % 100 != 0 and year % 4 == 0):
            return "true"
        else:
            return "false"

year = int(input("Enter Year : "))
print("{0} -> {1}".format(year, isLeapYear(year)))