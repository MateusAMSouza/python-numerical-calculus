import numpy as np

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter the entries in a single line (separated by space): ")
entries = list(map(float, input().split()))
matrix = np.array(entries).reshape(rows, columns)

squareMatrix = []

squareMatrix = [[(matrix[i][j]) for j in range(columns-1)] for i in range(rows)]

equationsResultsMatrix = [matrix[i][columns-1] for i in range(rows)]

'''
print(matrix)
print()
'''

determinant = np.linalg.det(squareMatrix)

n = columns - 1
columns = columns - 1


solution = [0] * n

if determinant == 0:
    print("It's not possible to use Gauss Elimination")
else:
    for k in range (n-1):
        for i in range (k+1, n):
            m = squareMatrix[i][k]/squareMatrix[k][k]
            squareMatrix[i][k] = 0
            for j in range (k+1, n):
                squareMatrix[i][j] = (squareMatrix[i][j] - (m * squareMatrix[k][j]))
            equationsResultsMatrix[i] = round(equationsResultsMatrix[i] - (m * equationsResultsMatrix[k]), 2)
    
    '''
    print(squareMatrix)
    print()
    print(equationsResultsMatrix)
    print()
    print(solution)
    '''
    
    n = n-1

    solution[n] = equationsResultsMatrix[n]/squareMatrix[n][n]
    for k in range(n-1, -1, -1):
        s = 0
        for j in range(k+1, n):
            s = s + squareMatrix[k][j]*solution[j]
        solution[k] = round((equationsResultsMatrix[k] - s)/squareMatrix[k][k], 2)

    print("The system solution is: ")
    print(solution)
