class Solution(object):
    def minTime(self, n, edgePairs, hasApple):
        
        edges = {}
        
        for (a,b) in edgePairs:
            # print(a,b)
            if a in edges:
                edges[a].append(b)
            else:
                edges[a] = [b]
            if b in edges:
                edges[b].append(a)
            else:
                edges[b] = [a]
        
        edges[0].append(-1)
        
        total = [0]
        visited = {}
        def recur(root,parent):
            if root in visited:
                # print(root)
                return
            visited[root] = True
            if len(edges[root])==1:
                if hasApple[root]:
                    return True
                else:
                    return False
            subTreeHasApple = hasApple[root]
            for child in edges[root]:
                if child is not parent:
                    isApple = recur(child,root)
                    if isApple:
                        total[0] += 2
                        subTreeHasApple = True
            # print(root,subTreeHasApple)
            return subTreeHasApple
    
        recur(0,-1)
        return total[0]
            
            
        