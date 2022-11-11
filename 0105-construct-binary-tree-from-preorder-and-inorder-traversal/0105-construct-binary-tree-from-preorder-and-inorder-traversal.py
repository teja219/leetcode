# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
  
        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(preorder[0])
        
        rval = preorder[0]
        root = TreeNode(rval)
        
        inorder_rval_index = inorder.index(rval)
        left_inorder = inorder[:inorder_rval_index]
        right_inorder = inorder[inorder_rval_index+1:]
        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[1 + len(left_preorder):]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root