'''

use a stack/list
if the first value is a closing brace return false

otherwise traverse the string
if you see an open brace push to the stack

if you see a close brace and the stack is empty return false

otherwise if you see a close brace
    pop from the stack and compare the two close brace values
    if they match opposite then continue
    otherwise return a false

if you get to the end and your stack is empty return true 
otherwise return false
2 mins
12 mins
Questions
will this contain non-brackets?
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == "]" or s[0] == "}" or s[0] == ')':
            return False
        dq = deque()
        for bracket in s:
            if self.isOpen(bracket):
                dq.append(bracket)
            elif not self.isOpen(bracket) and len(dq) == 0:
                return False
            else:
                curr = dq.pop()
                if self.bracketsMatch(curr, bracket):
                    continue
                else:
                    return False

        return len(dq) == 0

    def bracketsMatch(self, a, b):
        if a == "[" and b == "]" or a == "{" and b == "}" or a == "(" and b == ")":
            return True
        return False

    def isOpen(self, s):
        if s == "(" or s == "[" or s == "{":
            return True
        return False
