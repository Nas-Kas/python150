'''
find the pivot?
find an ascending sequence?

[2,4,5,6,7,0,1]
 s
       m      
             e

[6,7,0,1,2,4,5]
 s
       m
              e

if mids left and right are greater than you've found the pivot return it

if mid is less than start
- we know the right side is sorted
- so the pivot must be on the left side
- move to the side with the pivot?


if mid is greater than start
- we know the left side is in ascending order
- this means mid is a max of that value
- and start is possibly a min?

10 mins
34 mins
REVIEW THIS REVIEW THIS UNDERSTAND THIS* WRITE IT OUT BY HAND
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start  = 0
        end = len(nums) - 1
        mid = int(end / 2)

        if len(nums) == 1 or nums[start] < nums[end]:
            return nums[start]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        while start <= end:
            mid = int(start + (end - start) / 2)
            if self.checkMid(nums,mid):
                return nums[mid]
            elif nums[mid] < nums[0]:
                end = mid - 1
            else:
                start = mid + 1

        return nums[mid]

    def checkMid(self, arr, index):
        currVal = arr[index]
        if index == 0:
            return arr[index + 1] > currVal and arr[len(arr) - 1] > currVal
        elif index == len(arr) - 1:
            return arr[index - 1] > currVal and arr[0] > currVal
        else:
            return arr[index - 1] > currVal and arr[index + 1] > currVal 