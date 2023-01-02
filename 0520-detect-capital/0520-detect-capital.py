class Solution(object):
    def detectCapitalUse(self, word):
        wl = word.lower()
        wU = word.upper()
        
        if word==wU or word == wl:
            return True
        return word[:1].upper()==word[:1] and word[1:].lower()==word[1:]
        