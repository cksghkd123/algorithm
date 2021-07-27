n = int(input())
root = [1 for _ in range(n+1)]

link = [list() for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int,input().split())
    link[n1].append(n2)
    link[n2].append(n1)


que = [1]
visited = [False]*(n+1)
visited[1] = True

while que:
    select = que.pop()

    for next in link[select]:
        if visited[next] == False:
            que.append(next)
            root[next] = select
            visited[next] = True

for i in root[2:]:
    print(i)
