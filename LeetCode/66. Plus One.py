class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        an_integer = int(a_string)
        a_total = an_integer+1
        
        res = [int(x) for x in str(a_total)]
        return res
