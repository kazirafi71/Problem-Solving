class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = [int(x) for x in str(n)] 
        prod=1
        sum=0
        
        for i in res:
            prod=prod*i
            sum=sum+i
        
        return prod-sum