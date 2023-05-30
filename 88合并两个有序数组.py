def merge1(nums1, m, nums2, n):
    for i in range(n):
        nums1[m + i] = nums2[i]
    nums1.sort()


def merge2(nums1, m, nums2, n):
    nums1[:] = nums1[:m]
    nums1 += nums2
    nums1.sort()
    # 一行
    # nums1[:] = sorted(nums1[:m] + nums2) 