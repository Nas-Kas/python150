'''
use start and end pointers
slide down end if value is greater than target
increase start if value is less than target
return -1 if they collide
3 min
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            val = numbers[start] + numbers[end]
            if val == target:
                return [start + 1, end + 1]
            elif val < target:
                start += 1
            elif val > target:
                end -= 1
        