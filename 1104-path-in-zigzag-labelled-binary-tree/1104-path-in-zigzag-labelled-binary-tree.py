class Solution(object):
    def pathInZigZagTree(self, label):
        res = []
        while label!=0:
            res.append(label)
            h = int(floor(log(label,2)))
            label = (3*pow(2,h)-1-label)/2
        res.reverse()
        return res
            
        