# 8 Queens Problem using Backtracking

N = 8
board = [[0] * N for _ in range(N)]

qr, qc = map(int, input("Enter first queen position (row col): ").split())
qr -= 1
qc -= 1

def is_safe(row, col):
    for r in range(row):
        for c in range(N):
            if board[r][c] and (c == col or abs(row-r) == abs(col-c)):
                return False
    return True

def solve(row):
    if row == N:
        return True

    if row == qr:
        return is_safe(row, qc) and solve(row + 1)

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False

board[qr][qc] = 1

if solve(0):
    print("Solution:")
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
else:
    print("No solution exists.")
