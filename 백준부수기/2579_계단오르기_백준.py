import collections


n = int(input())
stairs_info = [None]
for _ in range(n):
    stairs_info.append(int(input()))

deq = collections.deque()
deq.append((0, 0, 0))
visited = [[0,0] for _ in range(n+1)]
answer = 0

while deq:
    here, score, count = deq.popleft()

    if here == n:
        answer = max(answer, score)
        continue
    
    if count<2 and here<n:
        new_here = here+1
        new_count = count+1
        new_score = score+stairs_info[new_here]
        if new_score > visited[new_here][new_count-1]:
            visited[new_here][new_count-1] = new_score
            deq.append((new_here, new_score, new_count))

    if here<n-1:
        new_here = here+2
        new_count = 1
        new_score = score+stairs_info[new_here]
        if new_score > visited[new_here][new_count-1]:
            visited[new_here][new_count-1] = new_score
            deq.append((new_here, new_score, new_count))

print(answer)