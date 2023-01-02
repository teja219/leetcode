# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        
        def recur(arr):
            if arr==[]:
                return [None]
            if len(arr)==1:
                return [TreeNode(arr[0],None,None)]
            results = []
            for i in range(len(arr)):
                leftAns = recur(arr[:i])
                rightAns = recur(arr[i+1:])
                
                for lTree in leftAns:
                    for rTree in rightAns:
                        root = TreeNode(arr[i],lTree,rTree)
                        results.append(root)
            return results
        
        return recur([i for i in range(1,n+1)])
                        
                        
                    
            
        