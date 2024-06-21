import collections


n, m = map(int, input().split())

prior_order = [set() for _ in range(n+1)]
in_degree = [set() for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    count, *order = map(int, input().split())
    
    for i in range(count-1):
        prior_order[order[i]].add(order[i+1])
        in_degree[order[i+1]].add(order[i])


for i in range(1, n+1):
    in_degree[i] = len(in_degree[i])

is_answered = False

deq = collections.deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        deq.append((i, 1))

result = []
while deq:
    curr_i, count = deq.popleft()
    if visited[curr_i]:
        continue
    visited[curr_i] = True
    result.append(curr_i)

    for i in prior_order[curr_i]:
        in_degree[i] -= 1

    for next_i in range(1, n+1):
        if in_degree[next_i] == 0 and not visited[next_i]:
            deq.append((next_i, count+1))

for i in range(1, n+1):
    if not visited[i]:
        print(0)
        break
else:
    for j in result:
        print(j)
