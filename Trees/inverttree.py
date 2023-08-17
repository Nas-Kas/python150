# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
remember to swap the nodes themselves not just the values
8 mins
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root):
        if root == None:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.traverse(root.left)
        self.traverse(root.right)