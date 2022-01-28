target = int(input())
n = int(input())
if n != 0:
    broken = list(map(int, input().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    if n == 0:
        min_count = min(min_count, len(str(target)))
        break

    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)