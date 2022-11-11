# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        
        def recur(root,d):
            if root is None:
                return (d,None)
            
            (ld,lN) = recur(root.left,d+1)
            (rd,rN) = recur(root.right,d+1)
            
            if ld==rd:
                return (ld,root)
            if ld>rd:
                return (ld,lN)
            else:
                return (rd,rN)
            
        return recur(root,0)[1]