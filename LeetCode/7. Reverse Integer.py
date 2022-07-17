class Solution:
    def reverse(self, x: int) -> int: 
        
        if x >= 2**31-1 or x <= -2**31: return 0
        Reverse = 0 
        x=str(x)
        y=''
        
        if x[0]=='-':
            a=x[::-1]
            p=int((a[:-1]))
            
            # for i in p:
            #     if i=='0':
            #         pass
            #     else:
            #         y=y+i
            
            if int(p) >= 2**31-1 or int(p) <= -2**31: return 0
            else:
                return f"{x[0]}{p}"     
            
        else:
            x=int(x)
            while((x) > 0):    
                Reminder = x %10    
                Reverse = (Reverse *10) + Reminder    
                x = x //10
            if int(Reverse) >= 2**31-1 or int(Reverse) <= -2**31: return 0
            else:
                return Reverse
                