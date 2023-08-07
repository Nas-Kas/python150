'''

traverse each index
for each index you need to know the max left and the max right
choose the min value between both of those
add it to a total?

  [0,1,0,2,1,0,1,3,2,1,2,1]
             *

ml[0,1,1,2,2,2,2,3,3,3,3,3]
mr[3,3,3,3,3,3,3,3,2,2,2,1]
               *
ml = 2
mr = 3
height = 1

min(ml,mr) - height =
total 2
10 mins
21 mins
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxL = 0
        maxR = 0
        total = 0
        for idx in range(len(height) - 1):
            maxL = max(maxL,height[idx])
            maxLeft[idx] = maxL

        for idx in range(len(height) -1, -1, -1):
            maxR = max(maxR,height[idx])
            maxRight[idx] = maxR

        for idx in range(len(height) - 1):
            minval = min(maxLeft[idx],maxRight[idx])
            total += minval - height[idx]

        return total