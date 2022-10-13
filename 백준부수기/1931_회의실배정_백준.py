import heapq
from this import d


n = int(input())
conference_info = []
for i in range(n):
    s, e = map(int,input().split())
    conference_info.append((s,e,i))
conference_info_byS = sorted(conference_info,key=lambda x:x[0])
conference_info_byE = sorted(conference_info,key=lambda x:(x[1],x[0]))

visited = [False for _ in range(n)]
current_time = 0
answer = 0


for i in range(n):
    s1, e1, i1 = conference_info_byS[i]
    s2, e2, i2 = conference_info_byE[i]
    visited[i2] = True
    if current_time <= s1 and visited[i1]:
        answer += 1
        current_time = e1

print(answer)
