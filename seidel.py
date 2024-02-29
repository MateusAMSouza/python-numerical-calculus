import numpy as np

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter the entries in a single line (separated by space): ")
entries = list(map(float, input().split()))
matrix = np.array(entries).reshape(rows, columns)

precision = float(input("Enter the stop condition (solution precision): "))

squareMatrix = np.array([[(matrix[i][j]) for j in range(columns-1)] for i in range(rows)])

equationsResultsMatrix = np.array([matrix[i][columns-1] for i in range(rows)])

n = columns - 1

for i in range(n):
    pivot = squareMatrix[i][i]
    squareMatrix[i][i] = 0
    for j in range(n):
        if(j != i):
            squareMatrix[i][j] = -1 * (squareMatrix[i][j]/pivot)
    equationsResultsMatrix[i] = round(equationsResultsMatrix[i]/pivot, 2)



'''
print(squareMatrix)
print()
print(equationsResultsMatrix)
print()
'''

error = 1.00
oldResults = equationsResultsMatrix.copy()
newResults = oldResults.copy()

while error > precision:
    for i in range (n):
        multiply = np.dot(squareMatrix[i], newResults)
        newResults[i] = multiply + equationsResultsMatrix[i]

    compareResults = abs(newResults - oldResults)
    error = max(compareResults) / max(abs(newResults))

    oldResults = newResults.copy()

print("The system solution (with error less than or equal to {}) is: ".format(precision))
print(oldResults)