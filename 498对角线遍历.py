# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

mat = [[2,3]]

## 可行但是复杂度有点高的解法（会导致执行超时）

def findDiagonalOrder(mat):
    reslut = []
    for a in range(len(mat) + len(mat[0])):
        temp = []
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if i + j == a - 1:
                    
                    if a % 2:
                            temp.append(mat[i][j])

                    else:
                            reslut.append(mat[i][j])
        reslut = reslut + temp[::-1]
    return reslut
## 常规的解法

def a(mat):
    m, n = len(mat),len(mat[0])
    x = y = 0
    re = [mat[x][y]]
    i = 0
    while len(re) != m*n:
        if i % 2:
            if x + 1 < m:
                x += 1
            else:
                y += 1
            i+=1
            re.append(mat[x][y])
            while y + 1 < n and x - 1 > -1:
                y += 1
                x -= 1
                re.append(mat[x][y])
        else:
            if y + 1 < n:
                y += 1
            else:
                x += 1
            i +=1
            re.append(mat[x][y])
            while x + 1 < m and y - 1 > -1:
                y -= 1
                x += 1
                re.append(mat[x][y])
    return re   
