def sort_key(x):
    return (-x[0], x[1])
N = int(input())
A_list = list(map(int, input().split()))


for i in range(N):
    A_list[i] = (A_list[i], i)

M = int(input())
B_list = list(map(int, input().split()))

for i in range(M):
    B_list[i] = (B_list[i], i)

A_list.sort(key=sort_key)

B_list.sort(key=sort_key)

a_i = 0
b_i = 0
a_real_i = 0
b_real_i = 0

result = []

while a_i < N and b_i < M:
    if A_list[a_i][1] < a_real_i:
        a_i += 1
        continue

    if B_list[b_i][1] < b_real_i:
        b_i += 1
        continue

    if A_list[a_i][0] == B_list[b_i][0]:
        result.append(A_list[a_i][0])
        a_real_i = A_list[a_i][1]
        b_real_i = B_list[b_i][1]
        a_i += 1
        b_i += 1
    elif A_list[a_i][0] < B_list[b_i][0]:
        b_i += 1
    else:
        a_i += 1

if len(result) == 0:
    print(0)
else:
    print(len(result))
    print(*result)