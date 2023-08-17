# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
level order traversal grab the right values
bfs
7 mins
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        q.append(root)
        levels = [] 
        res = []
        check = [1,2,3,4]
        while len(q) > 0:
            currLen = len(q)
            temp = []
            for i in range(0,currLen):
                curr = q.pop()
                if curr:
                    temp.append(curr.val)
                if curr and curr.left:
                    q.insert(0,curr.left)
                if curr and curr.right:
                    q.insert(0,curr.right)

            levels.append(temp)
        for x in levels:
            if len(x) >= 1:
                res.append(x[len(x) - 1])
        return res