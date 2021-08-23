from collections import defaultdict


def root(n1, no):
    if n1 == no:
        return
    count = 0
    for n_node in graph[n1]:
        if n_node == no:
            continue
        root(n_node, no)
        count += 1
    if count == 0:
        global score
        score += 1

    

n = int(input())
parents = list(map(int,input().split()))
graph = defaultdict(list)
ex_node = int(input())
score = 0
for i, node in enumerate(parents):
    if node == -1:
        top = i
    else:
        graph[node].append(i)
root(top, ex_node)
print(score)


        
