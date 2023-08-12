'''
store string 1 in a map
create a sliding window of size of string 2 and store those values in map2
have a sliding window of size of s1 traverse through the string
if the maps are equal return true
otherwise remove str[start] from map and increment start
increment str[end] and add the new end value to the map
compare again until end reaches len(s2)

time O(n)^2? how fast can you compare maps*
space O(n+m)

3 minutes
finish 24:39
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map1 = {}
        map2 = {}
        start = 0
        end = len(s1) - 1

        for x in range(len(s1)): ## populate first map
            s1val = s1[x]
            s2val = s2[x]
            if s1val not in map1:
                map1[s1val] = 1
            else:
                map1[s1val] += 1
            
            if s2val not in map2:
                map2[s2val] = 1
            else:
                map2[s2val] += 1

        while end < len(s2) - 1:
            startVal = s2[start]
            if map1 == map2:
                return True
            else:
                if map2[startVal] == 1:
                    map2.pop(startVal)
                else:
                    map2[startVal] -= 1
                start += 1
                end += 1
                endVal = s2[end]
                if endVal in map2:
                    map2[endVal] += 1
                else:
                    map2[endVal] = 1
        
        return map1 == map2