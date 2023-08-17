# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
inorder traversal*
3 scenarios (middle, left side, right side)

hashmap [node:node]
key is the child and the value is the parent
[2:6][8:6][0:2][4:2][3:4][5:4][7:8][9:8][6:root(-1)]

[2,6,-1]
[8,6,-1]

[2,6,-1]
[4,2,6,-1]

compare p and q

if current node equals p or equals q
    return current node
if my current node is greater than p and less than q
i've hit my value
if my current node is less than p and less than q
move right
if my current node is greater than p and greater than q
move left
8 mins

    2
   / \
  1   3

p = 3 (right) 
q = 1 (left)

     6
    / \
    2  8
p = 2 (left) 
q = 8 (right)
2 > 3
27 minutes
note you dont always know that p will be less than and q will be greater than
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = p
        if p.val > q.val:
            p = q
            q = temp

        while root:
            if p.val == root.val or q.val == root.val:
                return root
            if root.val > p.val and root.val < q.val:
                return root
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                root = root.left

        return root