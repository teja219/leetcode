# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        q = deque([])
        maxWidth = 1
        q.append((root,0))
        while len(q)!=0:
            maxWidth = max(maxWidth,abs(q[0][1]-q[-1][1])+1)
            currentLevelLength = len(q)
            for _ in range(currentLevelLength):
                r,w = q.popleft()
                if r.left is not None:
                    q.append((r.left,w*2))
                if r.right is not None:
                    q.append((r.right,w*2+1))
        return maxWidth
            
        
        
        