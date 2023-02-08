class Solution(object):
    def getRow(self, rowIndex1):
        
        def getNextRow(rowIndex):
            result = [rowIndex[0]]
            for i in range(1,len(rowIndex)):
                result.append(rowIndex[i]+rowIndex[i-1])
            result.append(rowIndex[-1])
            return result
        
        result = [1]
        for i in range(rowIndex1):
            result = getNextRow(result)
        return result
            