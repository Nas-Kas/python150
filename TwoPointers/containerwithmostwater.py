'''

use a start and end pointer
calculate the height by doing

length = end - start
height = min(arr[start],arr[end])

return length * height
use a maxValue to store/update the value are if its greater than the current max
6 minutes
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxVal = 0
        while start < end:
            area = (end - start) * min(height[start], height[end])
            maxVal = max(maxVal, area)
            if height[start] < height[end]:
                start += 1
            elif height[start] >= height[end]:
                end -= 1
        return maxVal