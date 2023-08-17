# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

bfs level order traversal with a queue
- for each level put the root in the queue
- when you pop off a value use it as the curr node
- for that popped value add the left and right children to a queue do this for the length of the queue before the pop
- add the curr nodes left and rights to a temp list
- add the temp list to a list of lists
- repeat until you've reached all the nodes
iterative/recursive for dfs and bfs


Questions
we want left to right
if a node is empty do you want to represent it as null/none or nothing
how do you want htis returned
will an empty list be an empty list inside a list or just a list
5 min
20 mins
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        res = []
        if root == None:
            return res
        q.append(root)
        while len(q) > 0:
            currLen = len(q)
            temp = []
            for x in range(0,currLen):
                curr = q.pop()
                if curr:
                    temp.append(curr.val)
                if curr and curr.left:
                    q.insert(0,curr.left)
                if curr and curr.right:
                    q.insert(0,curr.right)
            res.append(temp)
        
        return res
                