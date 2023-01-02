# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        isUniversal = [True]
        baseVal = [root.val]
        def recur(root):
            if isUniversal[0]==False:
                return
            if root is None:
                return
            if root.val != baseVal[0]:
                isUniversal[0] = False
                return
            recur(root.left)
            recur(root.right)
        recur(root)
        return isUniversal[0]
        