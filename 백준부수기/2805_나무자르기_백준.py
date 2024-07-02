N, M = map(int, input().split())

trees = list(map(int, input().split()))

left = 1
right = 2000000000

answer = 0

while left <= right:
    mid = (left + right) // 2

    amount = 0
    for tree in trees:
        if tree >= mid:
            amount += tree - mid
    
    if amount >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid -1


print(answer)