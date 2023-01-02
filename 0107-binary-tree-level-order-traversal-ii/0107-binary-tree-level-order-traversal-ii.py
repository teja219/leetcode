# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []
        q = deque([])
        q.append(root)
        results = []
        
        while len(q)!=0:
            levelNodes = len(q)
            currentLevel = []
            for _ in range(levelNodes):
                top = q.popleft()
                currentLevel.append(top.val)
                if top.left != None:
                    q.append(top.left)
                if top.right != None:
                    q.append(top.right)
            results.append(currentLevel)
        results.reverse()
        return results
                