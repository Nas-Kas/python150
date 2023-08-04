from typing import List
'''
Questions
what do you mean by same element if there are two 2's but they're at different indicies do they count as the same or different elements?
is ther a time and space complexity were aiming for?
what should we return if there is no possible answer?

Solutions
double for loop traverse all possible answers O(n^2)
store the value of one and use a hasmap[key:val] where key is target-arr[i] and val is the index and if the transpose exists
when you traverse return that as an array otherwise return false O(n) we can do this because the combination of two values to equal
target should be unique

map[3:0][2:1][]
t - 6

[3,2,4]
     *

map [2:0][]

- 9 
- [2,7,11,15]
     *
does target - arr[i] exist
    if no put in map [arr[i]][index]
else 
    return arr 
done explain 8 min
done code 14 mins
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            compose = target - nums[x]
            if compose in hashmap:
                temp = [hashmap[compose],x]
                return temp
            else:
                hashmap[nums[x]] = x