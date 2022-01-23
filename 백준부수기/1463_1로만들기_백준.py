import collections


n = int(input())
visited = collections.defaultdict(lambda: False)

def bfs(number):
    deq = collections.deque()
    deq.append((0, number))
    while deq:
        count, number = deq.popleft()
        if number == 1:
            return count
        if number%3 == 0 and visited[number//3] == False:
            visited[number//3] = True
            deq.append((count+1, number//3))
        if number%2 == 0 and visited[number//2] == False:
            visited[number//2] = True
            deq.append((count+1, number//2))
        if visited[number-1] == False:
            deq.append((count+1, number-1))

answer = bfs(n)
print(answer)