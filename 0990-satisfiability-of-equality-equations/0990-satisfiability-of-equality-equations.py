class Solution(object):
    def equationsPossible(self, equations):
        
        parent={}
        rank={}
        for x in equations:
            parent[x[0]]=x[0]
            parent[x[3]]=x[3]
            rank[x[0]]=0
            rank[x[3]]=0
        
        
        def getParent(x):
            if x==parent[x]:
                return x
            
            parent[x]=getParent(parent[x])
            return parent[x]
        
        def union(x,y):
            px = getParent(x)
            py = getParent(y)
            
            if rank[px]<rank[py]:
                parent[px]=py
            elif rank[px]>rank[py]:
                parent[py]=px
            else:
                rank[px]+=1
                parent[py]=px
            return
        
        for x in equations:
            if x[1]=='=':
                union(x[0],x[3])
        
        for x in equations:
            if x[1]=='!' and (getParent(x[0])==getParent(x[3])):
                return False
        return True
                
        