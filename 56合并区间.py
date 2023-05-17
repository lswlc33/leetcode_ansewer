# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
intervals = [[1,4],[2,3]]


def merge(intervals):
    intervals.sort()    # 对原数组进行排序
    r = []  # 创建一个新的列表
    r.append(intervals[0]) # 把原数组第一个加入新列表
    for i in intervals:     # 遍历排序过的数组 
        if i[0] <= r[-1][1]:   # 如果区间和新列表最后的区间重叠
            r[-1][1] = max(i[1],r[-1][1])   # 更新新数组最后一个区间的右边
        else:
            r.append(i)     # 加入新数组
    return r

# 压缩压缩
def merge1(intervals):
    r = [sorted(intervals)[0]]
    for i in sorted(intervals):
        if i[0] <= r[-1][1]:
            r[-1][1] = max(i[1],r[-1][1])
        else:
            r.append(i)
    return r


print(merge(intervals))