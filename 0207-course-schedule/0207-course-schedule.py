class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        edges = {}
        for (a,b) in prerequisites:
            if b in edges:
                edges[b].append(a)
            else:
                edges[b] = [a]
        
        visited = {}
        cycle=[False]
        def dfs(x):
            if x in visited:
                if visited[x]==1:
                    cycle[0]=True
                return
            visited[x]=1
            if x not in edges:
                visited[x]=2    
                return
            for y in edges[x]:
                dfs(y)
            visited[x]=2
            return
        
        for i in range(numCourses):
            if i not in visited:
                dfs(i)
                # print i,visited
        
        # print cycle[0]
        return not cycle[0]
        
        