import collections


def find_radius(start_node, connections, n):
    visited = [False for _ in range(n+1)]
    deq = collections.deque()
    deq.append((start_node, 0))
    visited[start_node] = True
    result = 0

    while deq:
        curr_node, amount = deq.popleft()
        if amount > result:
            result = amount

        for next_node, cost in connections[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                deq.append((next_node, amount+cost))
    
    return result

n = int(input())

connections = [[] for _ in range(n+1)]
is_leaf = [True for _ in range(n+1)]
for _ in range(n-1):
    n1, n2, v = map(int, input().split())
    is_leaf[n1] = False
    connections[n1].append((n2, v))
    connections[n2].append((n1, v))

answer = 0
for i in range(1, n+1):
    if is_leaf[i]:
        result = find_radius(i, connections, n)
        if result > answer:
            answer = result

print(answer)