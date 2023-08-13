'''
keep a maxval
sum the values in k sliding window
use a start pointer and end pointer
if the currtotal is greater than the maxval update the max val
subtract start from total increment start
increment end from total add end
repeat process until end reaches the end of array

time 2 mins
TIME LIMIT EXCEEDED LEARN HOW TO DO THIS WITH DEQUE?
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k
        maxVal = 0
        res = []
        for index in range(0,len(nums) - k + 1):
            res.append(max(nums[index: index + k]))
        

        return res