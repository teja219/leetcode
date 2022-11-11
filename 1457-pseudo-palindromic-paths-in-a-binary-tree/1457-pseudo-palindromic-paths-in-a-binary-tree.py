# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def pseudoPalindromicPaths (self, root):
        mp = {}
        count = [0]
        def recur(x,numberOfOdds):
            if x.val in mp:
                mp[x.val]+=1
                if mp[x.val]%2==1:
                    numberOfOdds += 1
                else:
                    numberOfOdds -= 1
            else:
                mp[x.val]=1
                numberOfOdds += 1
            
            if x.left is None and x.right is None:
                # print x.val,numberOfOdds 
                if numberOfOdds<=1:
                    count[0]+=1
            
            if x.left is not None:
                recur(x.left,numberOfOdds)
            if x.right is not None:
                recur(x.right,numberOfOdds)
            
            mp[x.val]-=1
            if mp[x.val]%2==1:
                    numberOfOdds += 1
            else:
                numberOfOdds -= 1
            return
        
        recur(root,0)
        return count[0]
                
                    
                
                
            
        