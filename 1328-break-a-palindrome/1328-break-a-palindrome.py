class Solution(object):
    def breakPalindrome(self, palindrome):
        if len(palindrome)==1:
            return ""
        if len(set(palindrome))==1 and palindrome[0]=='a' and len(palindrome)>1:
            return palindrome[:-1]+'b'
        for i in range(len(palindrome)):
            if palindrome[i]!='a' and not (len(palindrome)%2==1 and i==len(palindrome)//2):
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+"b"
        