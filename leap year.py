def leap_year():
    if n % 4 == 0:
        print("{0} is a Leap year ".format(n))
    else:
        print("{0} is not a leap year".format(n))

n = int(input("Enter a number : "))
leap_year()
