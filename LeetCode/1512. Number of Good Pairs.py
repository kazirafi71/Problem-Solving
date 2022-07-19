class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        dict_of_counts = {item:nums.count(item) for item in nums}
        print(dict_of_counts)
        sum=0
        for key in dict_of_counts:
            n=0
            n=(dict_of_counts[key]*(dict_of_counts[key]-1))//2
            sum+=n
            n=0
        
        return(sum)
        