board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]


def isValidSudoku(board):
    # 检查横向
    for i in range(9):
        temp = []

        for j in range(9):
            num = board[i][j]

            if num in temp:
                return False
            if num != ".":
                temp.append(num)

    # 检查竖向
    for i in range(9):
        temp = []

        for j in range(9):
            num = board[j][i]

            if num in temp:
                return False
            if num != ".":
                temp.append(num)

    # 检查九宫格
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            a = i
            temp = []

            while a < i + 3:
                b = j

                while b < j + 3:
                    num = board[a][b]

                    if num in temp:
                        return False
                    if num != ".":
                        temp.append(num)
                    b += 1
                a += 1

    return True


print(isValidSudoku(board))
