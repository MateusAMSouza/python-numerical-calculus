from torch.autograd.functional import jacobian
from torch import tensor
import numpy as np
import gauss_jordan as gj

def jordan(squareMatrix, equationsResultsMatrix):

    columns = len(squareMatrix[0]) + 1

    determinant = np.linalg.det(squareMatrix)

    n = columns - 1

    solution = [0] * n

    if determinant == 0:
        print("It's not possible to use Gauss Elimination")
    else:
        for k in range (n):
            for i in range (n):
                if(i != k):
                    m = squareMatrix[i][k]/squareMatrix[k][k]
                    squareMatrix[i][k] = 0
                    for j in range (n):
                        if(j != k):
                            squareMatrix[i][j] = (squareMatrix[i][j] - (m * squareMatrix[k][j]))
                    equationsResultsMatrix[i] = round(equationsResultsMatrix[i] - (m * equationsResultsMatrix[k]), 2)

        for i in range (n):
            solution[i] = round(equationsResultsMatrix[i]/squareMatrix[i][i], 2)

        #print("The system solution is: ")
        #print(solution)

        return(solution)


def f(x1, x2):
    return(4*x1 - x1**3 + x2, x1**2 / -9 + (4*x2 - x2**2) / 4 + 1)

x1 = tensor(-1, dtype = float)
x2 = tensor(-2, dtype = float)

jb = jacobian(f,(x1,x2))

'''
print(jb)
print()
print(x1.item())
print(jb[1][1].item())
print()
print(jb[1][1])
print()
'''

#squareMatrix = np.array([[(matrix[i][j]) for j in range(columns-1)] for i in range(rows)])
squareMatrix = np.array([[( jb[i][j].item() ) for j in range(2)] for i in range(2)])

'''
print(squareMatrix)
print()

print(f(-1, -2))
'''

equationsResultsMatrix = np.array([ (f(-1, -2)[i] * -1) for i in range(2)], float)

#print(equationsResultsMatrix)

precision = 0.05
error = 1.0
oldResults = np.array([-1, -2], float)
newResults = []

while error > precision and max(np.absolute(equationsResultsMatrix)) > precision:

    newResults = gj.jordan(squareMatrix, equationsResultsMatrix)
    newResults = np.add(newResults, oldResults)
    #print(newResults)

    compareResults = abs(np.subtract(newResults, oldResults))
    error = max(compareResults) / max(np.absolute(newResults))

    oldResults = newResults.copy()

    x1 = tensor(newResults[0], dtype = float)
    x2 = tensor(newResults[1], dtype = float)

    jb = jacobian(f,(x1, x2))

    squareMatrix = np.array([[( jb[i][j].item() ) for j in range(2)] for i in range(2)])
    equationsResultsMatrix = np.array([ (f(x1, x2)[i] * -1) for i in range(2)], float)


print("The system solution (with error less than or equal to {}) is: ".format(precision))
print(oldResults)