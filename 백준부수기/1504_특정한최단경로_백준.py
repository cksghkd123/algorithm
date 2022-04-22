import collections


def bfs(s_node):
    deq = collections.deque()
    if v1 == 1:
        deq.append((s_node,0,1))
        visited[s_node][1] = 0
    else:
        deq.append((s_node, 0, 0))
        visited[s_node][0] = 0
    score = INF

    while deq:
        node, amount, state = deq.popleft()
        for next_node, weight in graph[node]:
            if visited[next_node][state] > amount+weight:
                visited[next_node][state] = amount+weight
                if next_node == v1:
                    if state == 0:
                        new_state = 1
                    elif state == 2:
                        new_state = 3
                    else:
                        new_state = state
                elif next_node == v2:
                    if state == 0:
                        new_state = 2
                    elif state == 1:
                        if v2 == n:
                            score = min(score, amount+weight)
                            continue
                        new_state = 3
                    else:
                        new_state = state
                elif next_node == n and state == 3:
                    score = min(score, amount+weight)
                    continue
                else:
                    new_state = state
                deq.append((next_node,amount+weight,new_state))
    
    if score == INF:
        return -1
    else:
        return score
                

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    n1, n2, distance = map(int,input().split())
    graph[n1].append((n2,distance))
    graph[n2].append((n1,distance))
v1, v2 = map(int,input().split())

INF = float('inf')
visited = [[INF for _ in range(4)] for _ in range(n+1)]

answer = bfs(1)
print(answer)
