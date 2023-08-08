'''
pwwkew
^
 ^

start and end pointer
hashset to contain all unique values
while end is not equal to a value in the set
    add a new value to the set
    increment our end pointer
    update our max
while end is equal to a value in our set
    remove the value from the start
    increment our start pointer

update our max


Questions
will this only contain lowercase alphabet characters what to do about punctuation empty spaces etc.
can we have empty strings
4 mins
pwwkew
  *
  *
set[]
maxVal = 2
35 mins
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            print("top")
            return len(s)
        hashset = set()
        start = 0
        end = 1
        hashset.add(s[start])
        maxVal = 1
        while start <= end and end <= len(s) - 1:
            if s[end] not in hashset:
                hashset.add(s[end])
                end += 1
                maxVal = max(maxVal,len(hashset))
            elif s[end] in hashset:
                hashset.remove(s[start])
                start += 1
                maxVal = max(maxVal,len(hashset))

        maxVal = max(maxVal,len(hashset))
        return maxVal