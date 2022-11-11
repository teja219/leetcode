# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        
        def recur(preorder,inorder):
            if len(preorder)==0:
                return None
            if len(preorder)==1:
                return TreeNode(preorder[0],None,None)
            root = preorder[0]
            idx = 0
            for i in range(len(inorder)):
                if inorder[i]==root:
                    idx = i
                    break
                
            inorderLeft = inorder[:idx]
            inorderRight = inorder[idx+1:]
            
            preorderLeft = preorder[1:1+len(inorderLeft)]
            preorderRight = preorder[1+len(inorderLeft):]
            
            leftNode = recur(preorderLeft,inorderLeft)
            rightNode = recur(preorderRight,inorderRight)
            
            root = TreeNode(root,leftNode,rightNode)
            return root
        return recur(preorder,inorder)