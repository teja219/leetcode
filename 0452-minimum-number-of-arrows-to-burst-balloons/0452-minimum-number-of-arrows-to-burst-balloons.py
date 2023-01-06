class Solution(object):
    def findMinArrowShots(self, points):
        xs = []
        id_ = 0
        for (x1,x2) in points:
            xs.append((x1,0,id_))
            xs.append((x2,1,id_))
            id_ += 1
        
        xs.sort()
        
        ballonsBurst = set([])
        currentBaloons = set([])
        arrowsCount = 0
        for (p,isEnd,id_) in xs:
            if isEnd==0:
                currentBaloons.add(id_)
                currentBaloons.add(id_)
            else:
                if len(currentBaloons)>0 and id_ not in ballonsBurst:
                    arrowsCount += 1
                    ballonsBurst.update(currentBaloons)
                    currentBaloons = set([])
                    
                
        return arrowsCount
            
        