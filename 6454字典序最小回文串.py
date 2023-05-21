class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        s = list(s)
        a = 0

        while a <= len(s)//2:
            if s[a] < s[-1-a]:
                s[-1-a] = s[a]
            elif s[a] > s[-1-a]:
                s[a] = s[-1-a]
            a += 1

        res = ''.join(s)

        return res