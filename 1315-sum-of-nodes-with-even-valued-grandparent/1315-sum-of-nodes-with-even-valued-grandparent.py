# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        total = [0]
        def dfs(root,parent,grandparent):
            if grandparent is not None and grandparent%2==0:
                total[0] += root.val
            if root.left is not None:
                dfs(root.left,root.val,parent)
            if root.right is not None:
                dfs(root.right,root.val,parent)
            return
            
        dfs(root,None,None)
        return total[0]
        