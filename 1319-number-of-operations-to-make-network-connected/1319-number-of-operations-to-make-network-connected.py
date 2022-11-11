class Solution(object):
    def makeConnected(self, n, connections):
        
        parent = {}
        rank = {}
        additionalEdges = [0]
        
        for i in range(n):
            parent[i]=i
            rank[i]=0
            
        
        components = [n]
        def getParent(x):
            if x==parent[x]:
                return x
            else:
                parent[x]=getParent(parent[x])
                return parent[x]
        
        def union(x,y):
            (px,py) = (getParent(x),getParent(y))
            if px!=py:
                components[0]-=1
            if px==py:
                additionalEdges[0] += 1
            if rank[px]<rank[py]:
                parent[px]=py
            elif rank[py]<rank[px]:
                parent[py]=px
            else:
                rank[px]+=1
                parent[py]=px
            return
         
        for e in connections:
            union(e[0],e[1])
        # print components,additionalEdges
        if additionalEdges[0]<components[0]-1:
            return -1
        else:
            return components[0]-1
            
        
            
        