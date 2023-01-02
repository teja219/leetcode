# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root==None:
            return []
        q = deque([])
        q.append(root)
        
        result = []
        while(len(q)!=0):
            n = len(q)
            last = q[-1].val
            result.append(last)
            for _ in range(n):
                front = q.popleft()
                if front.left != None:
                    q.append(front.left)
                if front.right != None:
                    q.append(front.right)
            
            
        return result