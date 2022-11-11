# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        
        def recur(preorder,postorder):
            # print "preorder:",preorder,"postorder:",postorder
            if len(preorder)==0:
                return None
            if len(preorder)==1:
                return TreeNode(preorder[0],None,None)
            root = preorder[0]
#           Split postorder
            secondPreorder = preorder[1]
            idx = postorder.index(secondPreorder)
            # print "split postorder by idx:",idx
            leftPostOrder = postorder[:idx+1]
            rightPostOrder = postorder[idx+1:-1]
            # print "leftPostOrder:",leftPostOrder," rightPostOrder",rightPostOrder
            
#           Split preorder
            # print postorder
            t1 = len(leftPostOrder)
            # print "split preorder by t1:"
            leftPreorder = preorder[1:1+t1]
            rightPreorder = preorder[1+t1:]
            # print "leftPreorder:",leftPreorder," rightPreorder",rightPreorder
            
            leftNode = recur(leftPreorder,leftPostOrder)
            rightNode = recur(rightPreorder,rightPostOrder)
            
            return TreeNode(root,leftNode,rightNode)
        
        return recur(preorder,postorder)
        