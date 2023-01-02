# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        prevElement = [-100000000000000]
        isValid = [True]
        def inorder(root):
            if not isValid[0]:
                return
            if root==None:
                return
            inorder(root.left)
            if root.val<=prevElement[0]:
                isValid[0]=False
            prevElement[0]=root.val
            inorder(root.right)
        
        inorder(root)
        return isValid[0]
                
        