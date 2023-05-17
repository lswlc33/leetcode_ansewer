# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

matrix = [[5, 1, 9, 11],       #[15,13, 2, 5],
          [2, 4, 8, 10],       #[14, 3, 4, 1],
          [13,3 , 6, 7],       #[12, 6, 8, 9],
          [15,14,12,16]]       #[16, 7,10,11]

# 创建一个新矩阵来做
def rotate1(matrix):
    import copy
    n = len(matrix)   # 矩阵的边长
    r = copy.deepcopy(matrix)   # 复制一个矩阵
    for i in range(0,n):    # 根据新矩阵替换掉旧矩阵的数字
        for j in range(0,n):
            matrix[i][j] = r[n-1-j][i]
    return matrix

# 使用临时值来做来做
def rotate2(matrix):
    n = len(matrix)
    for i in range(0, n // 2):
        for j in range(0, n // 2):
            temp = matrix[i][j]  # 创建一个temp保存第一个数
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
    return matrix

print(rotate2(matrix))