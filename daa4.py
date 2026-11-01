n = int(input("Enter number of queens: "))
board = [[0 for _ in range(n)] for _ in range(n)]
row = int(input("Enter first queen row (1 to n): ")) - 1
col = int(input("Enter first queen column (1 to n): ")) - 1
def is_safe(row, col):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i == row or j == col or abs(i - row) == abs(j - col):
                    return False
    return True
def solve(row):
    if row == n:
        return True
    if row == first_row:
        return solve(row + 1)
    for col in range(n):
        if is_safe(row, col):
            board[row][col] = 1
            if solve(row + 1):
                return True
            board[row][col] = 0
    return False
first_row = row
board[row][col] = 1
if solve(0):
    print("\nN-Queens Solution:")
    for r in board:
        print(" ".join("Q" if x == 1 else "." for x in r))
else:
    print("No solution exists for the given first queen position.")