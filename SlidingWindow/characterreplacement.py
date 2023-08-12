'''
longest substring with at least k replacements
calculate the number of diff values?

sliding window
if validString
 update maxVal
 add end to map
 increment end
elif not validString
 remove start from map
 increment start

AABABBA
*
 *

given a string/map (isvalidString)
- find the key in the map with the highest frequency
- use that as my solid group
- count all the values in the map that arent that key
- if that value is greater than k we have an invalid/swappable string
- otherwise we have a valid/swappable string
6 min
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 1
        maxVal = 1
        hashmap = {}
        hashmap[s[start]] = 1
        while start <= end and end < len(s):
            if self.isValidString(hashmap,k):
                #print(s[start:end])
                if s[end] in hashmap:
                    hashmap[s[end]] += 1
                else:
                    hashmap[s[end]] = 1
                maxVal = max(maxVal, end - start)
                end += 1
            else:
                if hashmap[s[start]] > 1:
                    hashmap[s[start]] -= 1
                else:
                    hashmap.pop(s[start])
                start += 1
        if self.isValidString(hashmap,k):
            maxVal = max(maxVal, end - start)

        return maxVal



    def isValidString(self, hashmap, k):
        mostfreq = -1
        mostfreqchar = ""
        othervals = 0
        for x in hashmap:
            if hashmap[x] > mostfreq:
                mostfreq = hashmap[x]
                mostfreqchar = x
            othervals += hashmap[x]

        othervals -= mostfreq
        #print(f"most freq {mostfreq} othervals {othervals} k {k}")
        if othervals <= k:
            return True
        return False

        