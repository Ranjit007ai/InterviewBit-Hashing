def not_in_row(A,row):
    s = set()
    for i in range(0,9):
        if A[row][i] in s:
            return False
        else:
            if A[row][i] != '.':
                s.add(A[row][i])
    return True

def not_in_col(A,col):
    s = set()
    for i in range(0,9):
        if A[i][col] in s:
            return False
        else:
            if A[i][col] != '.':
                s.add(A[i][col])
    return True

def not_in_box(A,start_row,start_col):
    s = set()
    for i in range(0,3):
        for j in range(0,3):
            cur = A[i + start_row][j + start_col]
            if cur in s:
                return False
            else:
                if cur != '.':
                    s.add(cur)
    return True
def isvalid(A,row,col):
    return (not_in_row(A,row) , not_in_col(A,col) , not_in_box(A, row - row % 3 , col - col % 3 ) )
def isvalid_sudoku(A):
    for i in range(0,9):
        for j in range(0,9):
            if not isvalid(A,i,j):
                return False
    return True

# test case
A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
ans = isvalid_sudoku(A)
print(ans)