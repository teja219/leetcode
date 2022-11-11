# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        
        def recur(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            
            return (p.val == q.val) and recur(p.left,q.left) and recur(p.right,q.right)
        
        return recur(p,q)
        