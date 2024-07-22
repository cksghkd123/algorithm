N = int(input())

A = list(map(int, input().split()))

dp_forward = [1 for _ in range(N)]
dp_reverse = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp_forward[i] = max(dp_forward[i], dp_forward[j]+1)

for i in range(N):
    for j in range(i):
        if A[N-1-j] < A[N-1-i]:
            dp_reverse[N-1-i] = max(dp_reverse[N-1-i], dp_reverse[N-1-j]+1)
answer = 0

for i in range(N):
    answer = max(answer, dp_forward[i] + dp_reverse[i] - 1)

print(answer)
