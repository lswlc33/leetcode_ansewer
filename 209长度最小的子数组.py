
def minSubArrayLen1(target = 11, nums = [1,2,3,4,5]):
    a = 1
    b = 0
    r = len(nums) + 1

    while a <= len(nums):
        
        if sum(nums[b:a]) >= target:
            l = a - b
            r = min(l, r)
            b += 1
            a = b + 1
        else:
            a += 1

    if r == len(nums) + 1:
        return 0

    return r



def minSubArrayLen2(target = 80, nums = [1,2,3,4,5]):
        a, b = 1, 0
        
        l = len(nums) + 1

        while b <= len(nums) - 1 and a <= len(nums):
            print(nums[b:a],sum(nums[b:a]))
            if sum(nums[b:a]) >= target:
                l = min(l, a-b)
                b += 1
            else:
                a += 1

        if l == len(nums) + 1:
            return 0

        return l


def minSubArrayLen3(target = 80, nums = [1,2,3,4,5]):
    a, b = 0, 0
    
    l = len(nums) + 1

    suml = nums[0]

    while b <= len(nums) - 1 and a < len(nums):
        if suml >= target:
            suml -= nums[b]
            l = min(l, a-b+1)
            b += 1
        else:
            if a + 1 != len(nums):
                suml += nums[a+1]
            a += 1
            

    if l == len(nums) + 1:
        return 0

    return l



print(minSubArrayLen3())