# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
recursive*
have two traversals recursively one that goes to the left and one that goes to the right
compare them at each step
if they differ at all return false
otherwise if it traverses all the way through return true

iterative*
bfs both sides iteratively using a queue
if it differs return false

'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p,q)

    def traverse(self, rootA, rootB):
        qA = [rootA]
        qB = [rootB]
        while len(qA) > 0 and len(qB) > 0:
            aCurr = qA.pop(0)
            bCurr = qB.pop(0)

            if aCurr == None and bCurr != None or bCurr == None and aCurr != None:
                return False
            
            if aCurr and bCurr and aCurr.val != bCurr.val:
                return False

            if aCurr:   
                qA.append(aCurr.left)
                qA.append(aCurr.right) 
            if bCurr:    
                qB.append(bCurr.left)
                qB.append(bCurr.right)
                

        return len(qA) == len(qB)
        
        