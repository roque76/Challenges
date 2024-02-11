def isToeplitzMatrix(matrix):
    i = 1
    for line in matrix:
        if i <= len(matrix)-1:
            line.pop()
            secondLine = matrix[i]
            y = 1
            output = True
            for value in line:
                if value != secondLine[y]:
                    output = False
                    break
                y += 1
            if not output:
                return False
        i = i+1
    return True



matrix =[[1,2,3,4],[5,1,2,3],[9,5,1,2]]

if isToeplitzMatrix(matrix):
    print("The matrix is a Toeplitz matrix.")
else:
    print("The matrix is not a Toeplitz matrix.")