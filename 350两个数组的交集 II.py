nums1 = [1,7,2,1]
nums2 = [2,7]

# 暴力法
def intersect1(nums1, nums2):
    res = []
    for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i)
    return res

# 排序双指针
def intersect2(nums1, nums2):
    res = []
    a = b = 0
    nums1, nums2 = sorted(nums1), sorted(nums2)

    while a <= len(nums1) - 1 and b <= len(nums2) - 1:
        if nums1[a] > nums2[b]:
            b += 1
        elif nums1[a] < nums2[b]:
            a += 1
        else:
            res.append(nums1[a])
            a += 1
            b += 1
    return res


# 哈希表法