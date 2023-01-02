# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        minDiff = [10000000000]
        
        prevElement = [-10000000000000]
        
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            minDiff[0] = min(minDiff[0],abs(root.val-prevElement[0]))
            prevElement[0] = root.val
            inorder(root.right)
        
        inorder(root)
        return minDiff[0]
            
        