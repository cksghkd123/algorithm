import collections


v = int(input())
adjuction = {i+1:[] for i in range(v)}

leaf_nodes = []
is_leaf = [0 for _ in range(v+1)]

for _ in range(v):
    info = list(map(int,input().split()))
    node1 = info[0]
    if len(info) == 4:
        leaf_nodes.append(node1)
    for i in range(1, len(info)-1):
        if i%2 == 1:
            node2 = info[i]
        else:
            is_leaf[node2] += 1
            adjuction[node1].append((node2, info[i]))

amount = [0 for _ in range(v+1)]

deq = collections.deque()
answer = 0

for node in leaf_nodes:
    deq.append(node)

while deq:
    node = deq.popleft()
    for next_node, weight in adjuction[node]:
        if is_leaf[next_node] > 0:
            is_leaf[node] -= 1
            is_leaf[next_node] -= 1
            answer = max(answer, amount[next_node]+amount[node]+weight)
            if amount[next_node] < amount[node]+weight:
                amount[next_node] = amount[node]+weight
            if is_leaf[next_node] == 1:
                deq.append(next_node)


print(answer)

