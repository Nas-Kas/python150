class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == "+":
                a,b = stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(a + b)
            elif x == "-":
                a,b = stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(b - a)
            elif x == "/":
                a,b = stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(b / a)
            elif x == "*":
                a, b= stack.pop(), stack.pop()
                a = int(a)
                b = int(b)
                stack.append(a * b)
            else:
                stack.append(x)
        
        return int(stack[0])