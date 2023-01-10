class Solution(object):
    def minimumHealth(self, damage, armor):
        
        totalDamage = 0
        maxDamage = 0
        for d in damage:    
            maxDamage = max(maxDamage,d)
            totalDamage += d
        
        if maxDamage>=armor:
            maxDamage = armor
        
        return totalDamage - maxDamage + 1
        
        
            
        