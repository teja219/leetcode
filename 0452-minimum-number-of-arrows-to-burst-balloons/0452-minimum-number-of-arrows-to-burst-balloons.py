class Solution(object):
    def findMinArrowShots(self, points):
        xs = []
        id_ = 0
        points.sort()
        newpoints = []
        
        id_ = 0
        for [x1,x2] in points:
            newpoints.append((x1,x2,id_))
            id_ += 1
        
            
            
            
        for (x1,x2,id_) in newpoints:
            xs.append((x1,0,id_))
            xs.append((x2,1,id_))
            
        
        xs.sort()
        
        ballonsBurst = -1
        currentBaloons = -1
        arrowsCount = 0
        for (p,isEnd,id_) in xs:
            if isEnd==0:
                currentBaloons = id_
            else:
                if id_ > ballonsBurst:
                    arrowsCount += 1
                    ballonsBurst = currentBaloons
                    
                
        return arrowsCount
            
        