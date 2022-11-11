# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        mp = {}
        mp[0]=1  # In prefix sum problems, you must always append a zero sum element at the start, in this case we ignored and lead to an error
        count = [0]
        def dfs(x,totalTillNow,parent):
            # print x.val
            if x == None:
                return
            
            totalTillNow += x.val
            # print x.val,totalTillNow,parent
            remainingTarget = totalTillNow-targetSum
            if remainingTarget in mp:
                count[0] += mp[remainingTarget]
            if totalTillNow in mp:
                mp[totalTillNow] += 1
            else:
                mp[totalTillNow] = 1
            
            dfs(x.left,totalTillNow,x.val)
            dfs(x.right,totalTillNow,x.val)
            
            mp[totalTillNow]-=1
            totalTillNow -= x.val
            return
        
        dfs(root,0,-1)
        return count[0]
            
        