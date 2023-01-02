# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        # [L,R] = [-100000000000000,100000000000000]
        isValid = [True]
        def preorder(root,l,r):
            if isValid[0]==False:
                return
            if root==None:
                return
            if not (root.val>=l and root.val<=r):
                isValid[0] = False
                return
            preorder(root.left,l,root.val-1)
            preorder(root.right,root.val+1,r)
        
        preorder(root,-100000000000000,100000000000000)
        return isValid[0]
                
        