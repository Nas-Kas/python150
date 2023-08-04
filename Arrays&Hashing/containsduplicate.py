'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

possible ways to solve:
use a hashmap to count the duplicates
i can sort and traverse if i see two in a row return that number
put the values in a set and if theres a duplicate return true

Questions:
is the array sorted?
most efficient approach is using a set
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupeList = set()
        for x in nums:
            if x in dupeList:
                return True
            else:
                dupeList.add(x)
        return False

s = Solution()
nums = [1,2,3,4,5]
print(s.containsDuplicate(nums))