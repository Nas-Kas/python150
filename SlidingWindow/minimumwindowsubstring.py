'''
minimum window substring

s = "ADOBECODEBANC", t = "ABC"
              *
                 *
two maps tMap and sMap
populate tMap with t values
create a start and end pointer populate start pointer in sMap

while sMap does not contain all the values in tMap
increment end and add values to sMap
if sMap contains all values in tMap store that as a shortest string

while sMap does have all the values in tMap
record the value as a shortest string if shorter
remove/decrement start from map
increment start pointer

return a shortest string at end

helper method
- check if sMap contains all the values in tMap
- go through tMap and check if tMap value in sMap and tMapvalue >= sMap value
6 minutes
finished 40 minutes
TODO: OPTIMIZE THIS CODE USE LESS LINES MAKE IT FASTER
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        sMap = {}
        start = 0
        end = 1
        sMap[s[start]] = 1
        shortestString = ""
        shortestLen = 100000

        for val in t:
            if val in tMap:
                tMap[val] += 1
            else:
                tMap[val] = 1
        
        while end <= len(s) - 1:
            startVal = s[start]
            if self.containsMap(tMap,sMap):
                if shortestLen >= (end - start):
                    shortestLen = (end - start)
                    shortestString = s[start:end]
                if sMap[startVal] == 1:
                    sMap.pop(startVal)
                else:
                    sMap[startVal] -= 1
                start += 1
            else:
                endVal = s[end]
                if endVal in sMap:
                    sMap[endVal] += 1
                else:
                    sMap[endVal] = 1
                end += 1        
        
        while start < end:
            startVal = s[start]
            if self.containsMap(tMap,sMap):
                if shortestLen >= (end - start):
                    shortestLen = (end - start)
                    shortestString = s[start:end]
                if sMap[startVal] == 1:
                    sMap.pop(startVal)
                else:
                    sMap[startVal] -= 1
            start += 1


        return shortestString

    def containsMap(self, tMap, sMap):
        for x in tMap:
            if x not in sMap or sMap[x] < tMap[x]:
                return False
        return True