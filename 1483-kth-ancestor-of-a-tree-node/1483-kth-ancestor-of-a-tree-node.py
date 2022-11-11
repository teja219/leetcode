class TreeAncestor(object):
    def recur(self,node,k):
            # print node,k
            if (node,k) in self.dp:
                return self.dp[(node,k)]
            if k==-1:
                self.dp[(node,k)] = -1
                return self.dp[(node,k)]
            if k==0:
                self.dp[(node,k)] = self.parent[node]
                return self.dp[(node,k)]
            nextNode = self.recur(node,k-1)
            if nextNode == -1:
                self.dp[(node,k)]=-1
                return self.dp[(node,k)]
            self.dp[(node,k)] = self.recur(nextNode,k-1)
            return self.dp[(node,k)]
    def __init__(self, n, parent):
        self.n = n
        self.parent = parent
        self.dp = {}
        
        
        H = int(ceil(log(n)))# don't forget to add int before ceil as ceil gives a double ex: ceil(1.58)=2.0
        print H
        for i in range(n):
            for h in range(H+1):
                self.recur(i,h)
        # print self.dp
        # self.dp2 = dp
        
        
        
    def getKthAncestor(self, node, k):
        base = 0
        # if k>int(ceil(log(self.n))):
        #     return -1
        while k!=0:
            if k%2!=0:
                node = self.recur(node,base)
            if node==-1:
                return -1
            k = k/2
            base = base+1
        return node
        
    
        
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)