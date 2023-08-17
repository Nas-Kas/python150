# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
increment some value every time i go left or right as the depth
and decrement the value every time you go up the stack

recursive without a stack*
iterative with a stack* dfs
iterative with a queue* bfs store the node along with the level
or bfs level order traversal

Questions
can we expect the tree to be relatively balanced?
10 mins
'''
class Solution:
    maxD = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.traverse2(root,0)

    def traverse(self, root, depth):
        Solution.maxD = max(depth, Solution.maxD)
        if root == None:
            return
        
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)
        Solution.maxD = max(depth, Solution.maxD)

    def traverse2(self, root, depth):
        Solution.maxD = max(depth, Solution.maxD)
        if root == None:
            return depth
        
        return max(self.traverse2(root.left, depth + 1), self.traverse2(root.right, depth + 1))