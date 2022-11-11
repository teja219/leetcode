# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        q = deque([])
        ans = root.val
        q.append(root)
        level = 1
        count = 1
        while len(q)!=0:
            rotten = len(q)
            tempAns = 0
            for i in range(rotten):
                curr = q.popleft()
                tempAns += curr.val
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            if tempAns>ans:
                ans = tempAns
                level = count
            count += 1
        return level
        