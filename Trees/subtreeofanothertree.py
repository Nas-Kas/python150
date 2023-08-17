# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isSame = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        Solution.isSame = False
        self.traverse(root,subRoot)
        return Solution.isSame

    def traverse(self, root, subroot):
        if root == None:
            return

        if root.val == subroot.val and self.isSameTree(root,subroot):
            Solution.isSame = True

        self.traverse(root.left,subroot)
        self.traverse(root.right,subroot)



    def isSameTree(self, rootA, rootB):
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
        
        