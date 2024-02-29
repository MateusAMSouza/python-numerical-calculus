from bisection import bisection

def function (x):
    return (x**3.0 - 9*x + 3.0)

def diff_function (x):
    return (3*x**2 - 9)


print("To define an interval containing one of the functions roots using the bisection method, insert an initial interval:")
first = float(input("Enter the range's start: "))
last = float(input("Enter the range's end: "))
precision = float(input("Enter the stop condition (solution precision): "))

interval = bisection(first, last, precision)

x0 = float(input("Enter the initial approximation (the value must be inside the interval {}): ".format(interval)))
if not interval.contains(x0):
    print("The value is not in the interval's range")
else:
    precision = float(input("Enter the stop condition (solution precision): "))

    x1 = x0

    if (abs(function(x0)) >= precision):
        x1 = x0 - function(x0)/diff_function(x0)
    while(abs(function(x1)) >= precision and abs(x1 - x0) >= precision):
        x0 = x1
        x1 = x0 - function(x0)/diff_function(x0)



    print("One of the function's roots is: {}".format(x1))

