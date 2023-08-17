# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
store the path in a dfs and check if that path is good
if it is add the current node to a list of nodes

store the min and the max we've seen so far in the path?
(curr,min,max)
(3,3,3) - good 3
(1,1,3) - no 
(3,1,3) - good 3

(3,3,3) - no
(4,3,4) - good 4
(5,3,5) - good 5
(1,1,4) - no

8 min

(3,-1,3,[]) - append
(3,3,3)

'''
class Solution:
    c = 0
    def goodNodes(self, root: TreeNode) -> int:
        arr = []
        Solution.c = 0
        self.traverse(root,root.val,str(root.val))
        return Solution.c

    def traverse(self, root, maxVal, path):
        if root == None:
            return
        if self.checkPath(path):
            Solution.c += 1
        if root.right:
            self.traverse(root.right, maxVal, path + "," + str(root.right.val))
        if root.left:
            self.traverse(root.left, maxVal, path + "," + str(root.left.val))

    def checkPath(self, path):
        arr = path.split(",")
        maxVal = arr[len(arr) - 1]
        for x in range(len(arr) - 1):
            if int(arr[x]) > int(maxVal):
                return False
        return True
    
'''
Solution #2
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        arr = []
        self.traverse(root,root.val,arr)
        #print(arr)
        return len(arr)

    def traverse(self, root, maxVal, arr):
        if root == None:
            return

        if root.val >= maxVal:
            arr.append(root.val)
        
        self.traverse(root.left, max(root.val, maxVal),arr)
        self.traverse(root.right, max(root.val, maxVal),arr)