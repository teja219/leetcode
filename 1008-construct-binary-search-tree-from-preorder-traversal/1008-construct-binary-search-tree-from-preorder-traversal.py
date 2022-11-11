# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        
        def recur(preorder):
            if len(preorder)==0:
                return None
            if len(preorder)==1:
                return TreeNode(preorder[0],None,None)


            for i in range(1,len(preorder)):
                if preorder[i]>preorder[0]:
                    break
            if preorder[0]>preorder[-1]:
                i = len(preorder)
            
            preorderLeft = recur(preorder[1:i])
            preorderRight = recur(preorder[i:])
            
            print preorder[1:i],preorder[i:],i
            return TreeNode(preorder[0],preorderLeft,preorderRight)
        
        return recur(preorder)