'''
https://leetcode.com/problems/zigzag-conversion/description/

'''
'''
given 

PAYPALISHIRING

if num rows is 3
the output will be 
PAHNAPLSIIGYIR

logically it will look like

P   A   H   N
A P L S I I G
Y   I   R

PAY as one vertical
YPA as an upwards diagonal
ALI as a vertical
ISW as an upwards diagonal
HIR as a vertical
RIG as an upwards diagonal
NG as a vertical

the output only asks to return the three rows though so we may not need to actually calculate the diagonal

given with indexes
0 1 2 3 4 5 6 7 8 9 10 11 12 13
P A Y P A L I S H I R   I  N  G

if rows == 3
top part
PAHN corresponds to [0,4,8,12]
mid part
APLSIIG corresponds to [1,3,5,7,9,11,13]
last part
YIR corresponds to [2,6,10]

how do we determine the length?
goes until you reach the end, the next number would go out of bounds, or you're trying to use a index that already was used

so given n rows the first string starting point is 0
grab the 0th index then 0th + row + 1 etc.
0, 0+4, 4+4,8+4 etc

second row starting point? previous starting point + 1? so 1
grab the 1'st index and add row
1, 1 + 2, 3 + 2, 5+ 2, etc

third row starting point? previous starting point + 1? so 3?
increment value previous increment value + 1?
3, ???


for numRows = 4

s = "PAYPALISHIRING", numRows = 4
PINALSIGYAHRPI
P     I    N
A   L S  I G
Y A   H R
P     I

top
PIN = [0,6,12] incrementDistance = rows + 2
ALSIG = [1,5,7,11,13] incrementDistance = rows
YAHR = [2,4,8,10] incrementDistance = rows - 2
PI = [3,9] incrementDistance = rows + 2

'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] * numRows for i in range(numRows)]
        count = 0
        currArr = 0
        positive = True
        res = ""
        if numRows <= 1:
            return s
        while count < len(s):
            if positive:
                while currArr < len(matrix) - 1 and count < len(s):
                    matrix[currArr].append(count)
                    currArr += 1
                    count += 1
                positive = False
            else:
                while currArr > 0 and count < len(s):
                    matrix[currArr].append(count)
                    currArr -= 1
                    count += 1
                positive = True
        print(matrix)
        for x in matrix:
            for y in x:
                res += s[y]
        return res


s = Solution()
s1 = "PAYPALISHIRING"
s2 = "A"

print(s.convert(s1,3)) # "PAHNAPLSIIGYIR"
print(s.convert(s1,4)) # "PINALSIGYAHRPI"
print(s.convert(s2,1)) # A