# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        def recur(curr):
            if curr.left == None and curr.right == None:
                if curr.val == target:
                    return 1
                else:
                    return 0
            if curr.left != None:
                if recur(curr.left)==1:
                    curr.left = None
            if curr.right != None:
                if recur(curr.right)==1:
                    curr.right = None
            if curr.left == None and curr.right == None:
                if curr.val == target:
                    return 1
                else:
                    return 0
            
        r = recur(root)
        if r==1:
            return None
        else:
            return root
        
                
                
                
        
    
    
        