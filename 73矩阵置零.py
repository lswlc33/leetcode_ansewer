# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

 
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
# 记行记列杀
def setZeroes1(matrix): 
    # 初始化两个数组，用于记录每一行和每一列是否有零元素
    x ,y = [0]*len(matrix),[0]*len(matrix[0]) 
    # 遍历整个矩阵，如果当前元素为零，将对应的行和列的标记设为1
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])): 
            if matrix[i][j] == 0: 
                x[i] = y[j] = 1 
 
    # 再次遍历整个矩阵，将标记为1的行和列上的所有元素都设为零 
    for i in range(len(matrix)): 
        if x[i]: # 如果第i行上有零元素
            for j in range(len(matrix[0])): 
                matrix[i][j] = 0 # 将第i行上的所有元素都设为零 
 
    for i in range(len(matrix[0])): 
        if y[i]: # 如果第i列上有零元素
            for j in range(len(matrix)): 
                matrix[j][i] = 0 # 将第i列上的所有元素都设为零




# 记坐标杀
def setZeroes(matrix): 
    # 创建两个集合，用于记录每一行和每一列出现零元素的索引
    rows, cols = set(), set()
    # 遍历整个矩阵
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # 如果当前元素为零，记录行和列的索引
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
                 
    # 再次遍历整个矩阵
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # 如果当前行或列上出现了零元素，将对应的元素设为零
            if i in rows or j in cols:
                matrix[i][j] = 0

setZeroes1(matrix)
print(matrix)

