import sys
input=sys.stdin.readline

V=int(input())
graph=[[] for _ in range(V+1)]
for _ in range(V):
    temp=list(map(int, input().split()))
    for i in range(1,len(temp),2):
        if temp[i]==-1: break
        graph[temp[0]].append([temp[i],temp[i+1]])

visited=[False]*(V+1)
node,distance=0,0
ans=0
def dfs(num):
    global ans,node,distance
    print("answer = {}, node = {}, num = {}, distance = {}".format(ans,node,num,distance))
    visited[num]=True
    for v,d in graph[num]:
        if visited[v]: continue
        distance+=d
        if ans<distance:
            node=v
            ans=distance
        dfs(v)
        distance-=d
    visited[num]=False
    print("return!!")
    return 

dfs(1)
dfs(node)

print(ans)