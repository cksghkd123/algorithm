import collections


n, m = map(int,input().split())
relation = {i:[] for i in range(1,n+1)}
for i in range(m):
    p1, p2 = map(int,input().split())
    relation[p1].append(p2)
    relation[p2].append(p1)

def bfs(one):
    visited = [False for _ in range(n+1)]
    visited[one] = True
    deq = collections.deque()
    deq.append((one, 0))
    result = 0
    while deq:
        p1, relation_count = deq.popleft()
        for p2 in relation[p1]:
            if visited[p2] == False:
                visited[p2] = True
                result += relation_count+1
                deq.append((p2, relation_count+1))

    return one, result

answer = (0, float('inf'))
for i in range(1, n+1):
    one, result = bfs(i)
    if result < answer[1]:
        answer = (one, result)

print(answer[0])