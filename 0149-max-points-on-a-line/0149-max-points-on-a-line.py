class Solution(object):
    def maxPoints(self, points):
        
        maxTotal = 1
        for id1 in range(len(points)):
            for id2 in range(len(points)):
                if id1!=id2 and id1<id2:
                    x1,y1,c1 = points[id1][0],points[id1][1],1
                    x2,y2,c2 = points[id2][0],points[id2][1],1
                    total = c1+c2
                    if x1==x2:
                        for id3 in range(len(points)):
                            if id3!=id2 and id3!=id1 and points[id3][0]==x1:
                                total += 1
                    elif y1==y2:
                        for id3 in range(len(points)):
                            if id3!=id2 and id3!=id1 and points[id3][1]==y1:
                                total += 1
                    else:
                        slope = ((float)(y1-y2))/((float)(x1-x2))
                        for id3 in range(len(points)):
                            (x3,y3,c3) = (points[id3][0],points[id3][1],1)
                            if id3!=id2 and id3!=id1 and x3!=x1 and slope == ((float)(y1-y3))/((float)(x1-x3)):
                                total += c3
                    maxTotal = max(maxTotal,total)
                                
                        
        
        return maxTotal
            
        
                    
        
        