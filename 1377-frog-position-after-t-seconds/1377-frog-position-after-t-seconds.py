class Solution(object):
    def frogPosition(self, n, edges, T, target):
        probability = 1
        mp = {}
        for (a,b) in edges:
            if a in mp:
                mp[a].append(b)
            else:
                mp[a] = [b]
            if b in mp:
                mp[b].append(a)
            else:
                mp[b] = [a]
        
            
        visited = {}
        ans = [0.0]
        def dfs(x,prob,t):
            # print x,prob
            if x in visited:
                return
            visited[x]=1
            neighbours = 0.0
            if x in mp:
                for y in mp[x]:
                    if y not in visited:
                        neighbours += 1
            if x==target:
                if t<T and neighbours==0.0:
                    ans[0] = prob
                elif t==T:
                    ans[0] = prob
                    
            
            
            
            if neighbours==0:
                return
            for y in mp[x]:
                if y not in visited:
                    dfs(y,prob*(1/neighbours),t+1)
            return
        dfs(1,1.0,0)
        # print ans[0]
        return ans[0]
        