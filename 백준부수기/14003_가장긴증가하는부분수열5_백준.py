def bisect_left(input_list, target):
    left = 0
    right = len(input_list)

    while left < right:
        mid = (left + right) // 2

        if input_list[mid] < target:
            left = mid+1
        else:
            right = mid
    
    return left

N = int(input())
A = list(map(int, input().split()))

LIS = []
pos = [0] * N
prev = [-1] * N

for i in range(N):
    if not LIS or LIS[-1] < A[i]:
        if LIS:
            prev[i] = pos[len(LIS) - 1]
        LIS.append(A[i])
        pos[len(LIS) - 1] = i
    else:
        idx = bisect_left(LIS, A[i])
        LIS[idx] = A[i]
        pos[idx] = i
        if idx != 0:
            prev[i] = pos[idx - 1]
    
    print(f"LIS: {LIS}, pos: {pos}, prev: {prev}")

result = []
current = pos[len(LIS) - 1]
while current != -1:
    result.append(A[current])
    current = prev[current]

result.reverse()

print(len(result))
print(*result)
