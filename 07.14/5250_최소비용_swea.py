import collections

inf = float('inf')
def mst():
    distance = [[inf]*N for _ in range(N)]
    deq = collections.deque()
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    deq.append((0,0))
    distance[0][0] = 0

    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                cost = 1
                if H[nr][nc] > H[row][col]:
                    cost += H[nr][nc] - H[row][col]
                if distance[nr][nc] > distance[row][col] + cost:
                    distance[nr][nc] = distance[row][col] + cost
                    deq.append((nr,nc))
    
    return(distance[N-1][N-1])
    
    

T = int(input())
for i in range(T):
    
    N = int(input())
    H = [tuple(map(int,input().split())) for _ in range(N)]
    print('#{} {}'.format(i+1,mst()))