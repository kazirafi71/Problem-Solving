class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s1 = ""
        t1 = ""
        s1 = []
        s1[:0] = s   
        t1 = []
        t1[:0] = t
        
        while "#" in s1:
            x = s1.index("#")
            if s1[0]=="#":
                s1.pop(0)
                continue
            s1.pop(x)
            s1.pop(x-1)
            

        while "#" in t1:
            x = t1.index("#")
            if t1[0]=="#":
                t1.pop(0)
                continue
            t1.pop(x)
            t1.pop(x-1)
            


        str1 = ""
        str2 = ""
        str1 = ''.join(str(e) for e in s1)
        str2 = ''.join(str(e) for e in t1)
        

        if(str1 == str2):
            return True
        else:
            return False

