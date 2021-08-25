import collections


dr = [1, 2, 1, 2, -1 ,-2, -1, -2]
dc = [2, 1, -2, -1, 2, 1, -2, -1]
def knight(i, row, col, target):
    if row == target[0] and col == target[1]:
        return 0
    visited[row][col] = True
    deq = collections.deque()
    deq.append((row, col, 0))
    while deq:
        row, col, count = deq.popleft()
        for w in range(8):
            nr = row + dr[w]
            nc = col + dc[w]
            if nr == target[0] and nc == target[1]:
                return count+1
            if 0 <= nr < i and 0 <= nc < i:
                if visited[nr][nc] == False:
                    visited[nr][nc] = True
                    deq.append((nr,nc,count+1))
    
t = int(input())
for _ in range(t):
    i = int(input())
    visited = [[False for _ in range(i)] for _ in range(i)]
    r, c = map(int,input().split())
    target = list(map(int,input().split()))
    result = knight(i, r, c, target)
    print(result)

                    