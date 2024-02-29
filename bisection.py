import math

first = float(input("Enter the range's start: "))
last = float(input("Enter the range's end: "))
precision = float(input("Enter the stop condition (solution precision): "))

estimate_iterations = math.ceil((math.log(last - first) - math.log(precision)) / math.log(2))

def function (x):
    return (x**3.0 - x**2.0 - x - 1.0)

count = 0

while (last - first) > precision:
    M = function(first)
    mean = (first + last) / 2.0
    if (M * function(mean)) > 0:
        first = mean
    else:
        last = mean
    count += 1

print("The root is in this range: [{}, {}]".format(first, last))
print("Using the range's mean ({}), f(x) = {}".format(((first + last)/2), function((first + last)/2)))
print("The estimated number of interations requires was {} and the number of iterations required was {}".format(estimate_iterations, count))


    