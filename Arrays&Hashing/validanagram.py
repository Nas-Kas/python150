'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Questions
is this problem case sensitive how do you want me to deal with uppercase lowercase
will this problem have only english characters or will it have punctuations
how do you want me to deal with empty spaces
are we allowed to change the string

Solutions
sort both the strings and see if they're the same (may need to have a sanitize function) time On(log(n)) to sort strings space O(n)

put both strings into a hashmap and compare the hashmaps for equality time O(n) space O(n)

put one string into a map traverse the other string and remove values from the map if at the end the map is empty its an anagram
if the map tries to take more than it can handle than its or not empty at the end its false
'''
class Solution:
    def isAnagram(self, s: str, t: str):
        s = sorted(s)
        t = sorted(t)
        return s == t