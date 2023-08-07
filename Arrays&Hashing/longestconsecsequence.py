'''
sliding window? no order doesnt matter?

put all values in a set (1 pass)
second pass for each index check if the arr[index] + 1 and arr[index] - 1 exists in set
if it does remove and increment a counter for each one removed
check in both directions until you've exhausted it
keep a max count

Maxcount = 4
currCount = 1
arr [100,4,200,1,3,2]
            *


set (200)
5 mins
11 mins 13 seconds
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        maxCount = 0
        for x in nums:
            hashset.add(x)

        for val in nums:
            currCount = 1
            if val in hashset:
                currVal = val + 1
                while currVal in hashset:
                    hashset.remove(currVal)
                    currVal += 1
                    currCount += 1
                currVal = val - 1
                while currVal in hashset:
                    hashset.remove(currVal)
                    currVal -= 1
                    currCount += 1
            maxCount = max(maxCount,currCount)

        return maxCount
