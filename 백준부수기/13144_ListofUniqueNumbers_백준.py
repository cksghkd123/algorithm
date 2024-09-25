N = int(input())
numbers = list(map(int, input().split()))

number_idx = {}

for n in numbers:
    number_idx[n] = -1

answer = 0
left = -1

for right in range(N):
    if number_idx[numbers[right]] >= left:
        left = number_idx[numbers[right]]
    
    number_idx[numbers[right]] = right
    answer += right-left

print(answer)