# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        
        count = [0]
        def recur(root,maxTillNow):
            if root is None:
                return
            
            if root.val>=maxTillNow:
                count[0]+=1
            maxTillNow = max(maxTillNow,root.val)
            
            recur(root.left,maxTillNow)
            recur(root.right,maxTillNow)
            
            return
        
        recur(root,-10000000000000000000)
        return count[0]
        