# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        
        def recur(s):
            if len(s)==0:
                return None
            if len(s)==1:
                return TreeNode(s[0],None,None)
            
            size = len(s)

            leftNode = recur(s[:size/2])
            rightNode = recur(s[size/2+1:])
            return TreeNode(s[size/2],leftNode,rightNode)
        ls = []
        while head!=None:
            ls.append(head.val)
            head = head.next
        
        return recur(ls)
        
        
        