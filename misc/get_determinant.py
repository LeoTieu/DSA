def get_determinant(matrix):
    '''Function that gets the deteriminant of a matrix'''

    if len(matrix) == 2:
        # Base case
        # |a b|
        # |c d|
        # det = (a * d) - (b * c)
        return matrix[0][0] * matrix [1][1] - matrix[0][1] * matrix[1][0]
    
    # Creates a matrix with the size of n-1*n-1
    # where n = amount of rows in original matrix
    smallerMatrix = []
    for row in range(1,len(matrix)):
        smallerMatrix.append(matrix[row][1:])

    determinant = 0
    for column in range(len(matrix)):
        if column % 2 == 0:
            # Adds the product of the current element on the first line with
            # the determinant of the smaller matrix.
            determinant += matrix[0][column] * get_determinant(smallerMatrix)
        else:
            # Same as above but subtracts.
            determinant -= matrix[0][column] * get_determinant(smallerMatrix)
        
        # All submatrixes has been calculated. Therefore returning the determinant.
        if column == len(matrix) - 1:
            return determinant
        
        # Updates smallerMatrix for the next iteration. 
        for row in range(len(smallerMatrix)):
            smallerMatrix[row][column] = matrix[row+1][column]

if __name__ == '__main__':
    myMatrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    myMatrix2 = [
        [1,2,3,4], 
        [5,6,6,8],
        [9,3,2,12],
        [13,14,4,16]
    ]

    myMatrix3 = [
        [7,3,7,0,2],
        [0,3,1,7,3],
        [1,8,0,2,8],
        [1,8,5,3,2],
        [0,2,1,6,0]
    ]

    print(get_determinant(myMatrix))  # 0
    print(get_determinant(myMatrix2)) # -672
    print(get_determinant(myMatrix3)) # -3057