'''
https://leetcode.com/problems/shuffle-the-array/description/
store in two seperate arrays and traverse both at the same time as references to overwrite values in the original arrays

nums = [2,5,1,3,4,7], n = 3
          ^
a = [2,5,1] 
       ^ 
b = [3,4,7]
     ^


two pointers without seperate arrays
nums = [2,5,1,3,4,7]
nums = [2,5,1,3,4,7]


nums = [2,3,5,4,1,7] 
       [0,3,1,4,2,5]

         
'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s1 = 0
        s2 = n
        copy = []
        flag = True
        for x in range(0, len(nums)):
            if flag:
                copy.append(nums[s1])
                flag = False
                s1 += 1
            else:
                copy.append(nums[s2])
                flag = True
                s2 += 1
        
        return copy
        