class Solution(object):
    def halvesAreAlike(self, s):
        mp = {}
        mp['a']=0
        mp['e']=0
        mp['i']=0
        mp['o']=0
        mp['u']=0
        mp['A']=0
        mp['E']=0
        mp['I']=0
        mp['O']=0
        mp['U']=0
        
        total1 = 0
        for c in s[:len(s)/2]:
            if c in mp:
                total1+=1
        
        for c in s[len(s)/2:]:
            if c in mp:
                total1-=1
        
        return total1==0
        
        