# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        def recur(root):
            if root.left is None and root.right is None:
                return (0,root.val,root.val)

            (ans,minTillNow,maxTillNow) = (0,root.val,root.val)

            if root.left is not None:
                (tempAns,tempMinTillNow,tempMaxTillNow) = recur(root.left)
                minTillNow = min(minTillNow,tempMinTillNow)
                maxTillNow = max(maxTillNow,tempMaxTillNow)

                ans = max(abs(root.val-minTillNow),abs(root.val-maxTillNow),tempAns,ans)

            if root.right is not None:
                (tempAns,tempMinTillNow,tempMaxTillNow) = recur(root.right)
                minTillNow = min(minTillNow,tempMinTillNow)
                maxTillNow = max(maxTillNow,tempMaxTillNow)

                ans = max(abs(root.val-minTillNow),abs(root.val-maxTillNow),tempAns,ans)

            return (ans,minTillNow,maxTillNow)
        
        (ans,_,_) = recur(root)
        return ans
        
            