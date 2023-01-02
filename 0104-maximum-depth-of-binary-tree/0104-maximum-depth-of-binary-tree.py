# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        maxLen = [0]
        
        def recur(root,d):
            if root == None:
                return
            maxLen[0] = max(maxLen[0],d)
            recur(root.left,d+1)
            recur(root.right,d+1)
        recur(root,1)
        return maxLen[0]
        