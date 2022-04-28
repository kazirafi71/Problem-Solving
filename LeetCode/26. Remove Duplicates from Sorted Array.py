class Solution:
    def removeDuplicates(self, nums):
        set_nums = set(nums)
        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
            else:
                num = "_"

        set_nums = sorted(set_nums)

        nums[:len(set_nums)] = set_nums
        nums[len(set_nums):] = "_"

        return len(set_nums)
