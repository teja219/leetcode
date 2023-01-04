class Solution(object):
    def multiply(self, num1, num2):
        
        def add(x1,x2):
            if len(x1)<len(x2):
                temp = x1
                x1 = x2
                x2 = temp
            diff = len(x1)-len(x2)
            
            for _ in range(diff):
                x2 = "0" + x2
            
            ans = ""
            carry = 0
            # print(x1,x2)
            for i in reversed(range(len(x1))):
                # print(ans)
                temp = int(x1[i])+int(x2[i])+carry
                ans = str(temp%10)+ans
                carry = temp/10
            
            if carry!=0:
                ans = str(carry) + ans
            
            return ans
        
        
        def multiply(t1,x):
            carry = 0
            ans = ""
            for i in reversed(range(len(t1))):
                # print(ans)
                temp = int(t1[i])*int(x)+carry
                ans = str(temp%10)+ans
                carry = temp/10
            if carry!=0:
                ans = str(carry)+ans
            return ans
        
        
        zeroes = ""
        total = "0"
        for i in reversed(range(len(num2))):
            total = add(multiply(num1,num2[i])+zeroes,total)
            zeroes = "0"+zeroes
        return str(int(total))
        