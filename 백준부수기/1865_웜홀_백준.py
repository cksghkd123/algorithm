import collections

def find(first_node):
    visited = [INF for _ in range(n+1)]
    deq = collections.deque()
    deq.append((first_node, 0))
    visited[first_node] = 0

    while deq:
        node, amount = deq.popleft()
        for next_node, cost in roads[node]:
            new_amount = amount+cost
            if next_node == first_node and new_amount < 0:
                global answer
                answer = 'YES'
                return
            if visited[next_node] > new_amount:
                visited[next_node] = new_amount
                deq.append((next_node, new_amount))

tc = int(input())
INF = float('inf')
for _ in range(tc):
    n, m, w = map(int,input().split())
    roads = [[] for _ in range(n+1)]
    holes = []
    deq = collections.deque()

    for _ in range(m):
        s, e, t = map(int,input().split())
        roads[s].append((e,t))
        roads[e].append((s,t))
    for _ in range(w):
        s, e, t = map(int,input().split())
        holes.append((s,e,t))
        roads[s].append((e,-t))
    
    answer = 'NO'
    for s, e, t in holes:
        find(e)
        if answer == 'YES':
            break
    
    print(answer)
    
            