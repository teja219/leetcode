# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        res = [""]
        
        def dfs(x,tillNow):
            
            # if res[0] != "" and len(res[0])<len(tillNow):
            #     return
            tillNow = tillNow + chr(ord('a')+x.val)
            if x.left == None and x.right==None:
                tillNow = tillNow[::-1]
                if res[0] != "":
                    res[0] = min(res[0],tillNow)
                else:
                    res[0] = tillNow
                return
            
            
            # print tillNow,chr(ord('a')+x.val)
            if x.left is not None:
                dfs(x.left,tillNow)
            if x.right is not None:
                dfs(x.right,tillNow)
            return
        
        dfs(root,"")
        
        return res[0]
            
            
                
            
        