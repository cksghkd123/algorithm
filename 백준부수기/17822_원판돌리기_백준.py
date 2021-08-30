from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def bfs(init_row, init_col, number):
    button = False
    deq = deque()
    deq.append((init_row, init_col))
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = (col + dc[w]) % m
            if 0 <= nr < n:
                if circles[nr][nc] == number:
                    circles[init_row][init_col] = 0
                    button = True
                    circles[nr][nc] = 0
                    deq.append((nr,nc))
    
    return button

n, m, t = map(int,input().split())
circles = [deque(map(int,input().split())) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int,input().split())
    number = x
    while number <= n:
        if d == 0:
            for _ in range(k):
                circles[number-1].appendleft(circles[number-1].pop())
        elif d == 1:
            for _ in range(k):
                circles[number-1].append(circles[number-1].popleft())
        number += x

    bbb = False
    count = 0
    for row in range(n):
        for col in range(m):
            if circles[row][col] != 0:
                bb = bfs(row, col, circles[row][col])
                if bb == True:
                    bbb = True
                else:
                    count += 1

    if bbb == False:
        if count == 0:
            break
        ave = sum(list(sum(circles[i]) for i in range(n))) / count
        for row in range(n):
            for col in range(m):
                if circles[row][col] != 0:
                    if circles[row][col] > ave:
                        circles[row][col] -= 1
                    elif circles[row][col] < ave:
                        circles[row][col] += 1
                
    

answer = sum(list(sum(circles[i]) for i in range(n)))
print(answer)
