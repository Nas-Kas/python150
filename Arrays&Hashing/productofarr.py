'''
[1,2,3,4] -> [   24,    12,      8,      6   ]
[a,b,c,d] -> [(b*c*d),(a*c*d),(a*b*d),(a*b*c)]

inarr
       [1, 2, 6, 24]
outarr [24,24,12, 4]
                  *
[24,12,8,6]
[(a),(a*b),(a*b*c),(a*b*c*d)]
[(d),(d*c),(d*c*b),(d*c*b*a)]

[(b*c*d),(a*c*d),(a*b*d),(a*b*c)]

r 6 min
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        inarr = []
        outarr = []
        res = []
        for x in range(len(nums)):
            inarr.append(nums[x])
            outarr.append(nums[x])

        for x in range(len(nums)):
            if x > 0:
                inarr[x] = inarr[x] * inarr[x - 1]
        for x in range(len(nums)-1, -1, -1):
            if x < len(nums) - 1:
                outarr[x] = outarr[x] * outarr[x + 1]
        print(inarr)
        print(outarr)
        for x in range(len(nums)):
            if x == 0:
                res.append(outarr[x + 1])
            elif x == len(nums) - 1:
                res.append(inarr[x - 1])
            else:
                res.append(inarr[x - 1] * outarr[x + 1])

        return res