class Solution(object):
    def spiralOrder(self, matrix):
        results=[]        
        def recur(matrix,rT,rB,cL,cR):
            # print(rT,rB,cL,cR)
            if rT>rB or cL>cR:
                return
            if rT==rB:
                # print(matrix[rT][cL:cR+1])
                for x in matrix[rT][cL:cR+1]:
                    results.append(x)
                return
            if cL==cR:
                for i in range(rT,rB+1):
                    results.append(matrix[i][cL])
                return
            results.extend(matrix[rT][cL:cR+1])
            
            for i in range(rT+1,rB):
                results.append(matrix[i][cR])
                
            temp = matrix[rB][cL:cR+1]
            temp.reverse()
            results.extend(temp)
            
            for i in reversed(range(rT+1,rB)):
                results.append(matrix[i][cL])
            
            recur(matrix,rT+1,rB-1,cL+1,cR-1)
        
        recur(matrix,0,len(matrix)-1,0,len(matrix[0])-1)
        return results