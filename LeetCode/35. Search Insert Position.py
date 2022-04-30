import sys

nums = list(map(int, input().split()))
target = int(input())

if target in nums:
    print(nums.index(target))
elif  nums[0]>target:
    print(0)
else:
    for i in range(0, len(nums)-1):

        if abs(nums[i]-target) == 1 and nums[i]+1 == target:
            print(i+1)
            sys.exit()
        elif nums[i] > target and nums[i+1] < target:
            print(i+1)
            sys.exit()
        elif nums[len(nums)-1] < target:
            print(len(nums))
            sys.exit()
        elif nums[i] < target and nums[i+1] > target:
            print(i+1)
            sys.exit()

    else:
        print(len(nums))
