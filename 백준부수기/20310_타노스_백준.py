S  = input()
n = len(S)

count_1 = 0
count_0 = 0 

for c in S:
    if c == '1':
        count_1 += 1
    elif c == '0':
        count_0 += 1

visited = [True for _ in range(n)]

target_count = count_1 // 2
count = 0

for i in range(n):
    if S[i] == "1":
        visited[i] = False
        count += 1
    
    if count == target_count:
        break

target_count = count_0 // 2
count = 0

for i in range(n-1, -1, -1):
    if S[i] == "0":
        visited[i] = False
        count += 1
    
    if count == target_count:
        break

for i in range(n):
    if visited[i]:
        print(S[i], end="")