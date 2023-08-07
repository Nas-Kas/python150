'''
sort the values
use a base as the first pointer
sort for the two values that add up to zero with the base
using the base as the starting point and the length of the array as the end point
if they add up to zero add to the bigger list

[-1,0,1,2,-1,-4]

[-4,-1,-1,0,1,2]
  b
     s
              e
 -4 + -1 + 2 = -3
12 mins
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(0,len(nums) - 1):
            base = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = base + nums[start] + nums[end]
                if total == 0:
                    temp = [base,nums[start], nums[end]]
                    if temp not in res:
                        res.append(temp)
                    start += 1
                elif total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
        return res