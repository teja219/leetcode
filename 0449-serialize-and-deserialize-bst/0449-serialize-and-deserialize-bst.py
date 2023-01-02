# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def recurSer(root):
            if root == None:
                return ""
            result = str(root.val)
            result += ","
            result = result + recurSer(root.left)
            result += ","
            result += recurSer(root.right)
            return result
        z = recurSer(root)
        print(z)
        return z

    def deserialize(self, data):
        numbersTemp = data.split(",")
        numbers = []
        for x in numbersTemp:
            if x!="":
                numbers.append(int(x))
        print(numbers)
        def deserializeRecur(numbers):
            if len(numbers)==0:
                return None
            if len(numbers)==1:
                return TreeNode(numbers[0],None,None)
            root = numbers[0]
            rootNode = TreeNode(numbers[0],None,None)
            
            
            found = 0
            i = bisect.bisect_left(numbers[1:],numbers[0])+1
            rootNode.left = deserializeRecur(numbers[1:i])
            rootNode.right = deserializeRecur(numbers[i:])
            return rootNode
        
        return deserializeRecur(numbers)
                        
        
    
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans