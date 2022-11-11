# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        def dfs(x,tillNow):
            tillNow.append(str(x.val))
            # print tillNow
            if x.left is None and x.right is None:
                # print tillNow
                # res.append(tillNow) --> This is wrong as python is pass by reference, so tillNow will vary
                res.append(tillNow[:])
                # print res
            else:
                if x.left is not None:
                    dfs(x.left,tillNow)
                if x.right is not None:
                    dfs(x.right,tillNow)
            tillNow.pop()
        
        dfs(root,[])
        res = ["->".join(ans) for ans in res]
        return res
            
                