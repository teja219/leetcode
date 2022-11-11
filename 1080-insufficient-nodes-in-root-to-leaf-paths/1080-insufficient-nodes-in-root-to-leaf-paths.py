# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        def recur(root,tillNow):
            tillNow += root.val
            if root.left is None and root.right is None:
                if tillNow<limit:
                    return 0
                else:
                    return 1
            l = 0
            r = 0
            if root.left is not None:
                l = recur(root.left,tillNow)
                if l==0:
                    root.left = None
            if root.right is not None:
                r = recur(root.right,tillNow)
                if r==0:
                    root.right = None
            
            if l==0 and r==0:
                return 0
            else:
                return 1
        x = recur(root,0)
        if x==0:
            return None
        return root
            
        
        
        