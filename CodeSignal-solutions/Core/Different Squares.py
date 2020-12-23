def differentSquares(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    diff_squares = dict()
    
    for i in range(rows-1):
        for j in range(columns-1):
            row1 = tuple(matrix[i][j:j+2])
            row2 = tuple(matrix[i+1][j:j+2])
            diff_squares[(row1, row2)] = None
    
    return len(diff_squares)
