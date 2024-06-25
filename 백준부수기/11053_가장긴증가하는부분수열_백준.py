N = int(input())
A = list(map(int, input().split()))

count = [0 for _ in range(N)]

count[0] = 1

answer = 0

for i in range(N):
    count[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            count[i] = max(count[i], count[j]+1) 
    
    answer = max(answer, count[i])

print(answer)