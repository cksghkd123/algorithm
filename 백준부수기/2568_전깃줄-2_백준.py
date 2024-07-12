def bisect_left(input_list, target):
    left = 0
    right = len(input_list)

    while left < right:
        mid = (left + right) // 2

        if input_list[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


n = int(input())

line_list = [list(map(int, input().split())) for _ in range(n)]

line_list.sort()
LIS = []
pos = [0] * n
prev = [-1] * n

for i in range(n):
    if not LIS or LIS[-1] < line_list[i][1]:
        if LIS:
            prev[i] = pos[len(LIS) - 1]
        LIS.append(line_list[i][1])
        pos[len(LIS) - 1] = i    
    else:
        idx = bisect_left(LIS, line_list[i][1])
        LIS[idx] = line_list[i][1]
        pos[idx] = i
        if idx != 0:
            prev[i] = pos[idx - 1]

result = []
current = pos[len(LIS) - 1]

while current != -1:
    result.append(line_list[current][0])
    current = prev[current]

result = set(result)

answer = []
for a, b in line_list:
    if a not in result:
        answer.append(a)

print(len(answer))
for a in answer:
    print(a)



# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6