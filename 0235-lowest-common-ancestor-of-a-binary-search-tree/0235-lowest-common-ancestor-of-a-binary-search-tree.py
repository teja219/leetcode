# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def recur(root,p,q):
            if p.val>q.val:
                tmp = p
                p = q
                q = tmp
            
            if p.val<=root.val and q.val>=root.val:
                return root
            elif root.val<p.val:
                return recur(root.right,p,q)
            else:
                return recur(root.left,p,q)
        return recur(root,p,q)
            
                
        