'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

building a map where the key is the sorted string
and the value is a list of strings that are anagrams of that string
ex.
build the map
- traverse through input
- for each input have a sorted string and unsorted string
- if the sorted string is in the map as a key
    - append the unsorted string to the list of values associated with that key
- if not 
    - create a new key that is the sorted string
    - add the unsorted string to the list of values associated with that key

- create a res list
- traverse through the map
- add the list of values to the res list one at a time

aet:[eat,tea,ate] [ant]:[nat,tan] [abt]:[bat]

traverse through map and put each list into a an array
return the array
6 mins

'''
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        res = []
        for x in strs:
            sortedString = ''.join(sorted(x))
            unsortedString = x
            if sortedString in sortedMap:
                sortedMap[sortedString].append(unsortedString)
            else:
                sortedMap[sortedString] = [unsortedString]
        
        for x in sortedMap:
            res.append(sortedMap[x])
        return res
        