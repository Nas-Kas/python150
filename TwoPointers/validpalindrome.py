'''
11 minutes
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.cleanStr(s)
        print(s)
        rev = s[::-1]
        print(rev)
        return rev == s

    def cleanStr(self, s: str) -> str:
        res = ""
        for x in s:
            if x.isalpha() or self.isNumber(x):
                res += x.lower()
        return res
    def isNumber(self, s: str):
        nums = ["1","2","3","4","5","6","7","8","9","0"]
        return s in nums
