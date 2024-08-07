import collections


def bfs(i):
    visited[i] = True
    result = candy_list[i]
    member = 1

    deq = collections.deque()
    deq.append(i)

    while deq:
        curr = deq.popleft()

        for nxt in friend_connetions[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                deq.append(nxt)
                result += candy_list[nxt]
                member += 1
    
    return result, member

N, M, K = map(int, input().split())

candy_list = list(map(int, input().split()))
friend_connetions = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    friend_connetions[a].append(b)
    friend_connetions[b].append(a)

group_info = []
visited = [False for _ in range(N)]

for i in range(N):
    if not visited[i]:
        candy_count, member_count = bfs(i)
        group_info.append((candy_count, member_count))

dp = [0 for _ in range(K)]

for candy_count, member_count in group_info:
    for k in range(K-1, member_count - 1, -1):
        dp[k] = max(dp[k], dp[k - member_count] + candy_count)

answer = max(dp)


print(answer)