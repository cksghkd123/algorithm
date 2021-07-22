from collections import deque


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def find_cus(man, init_fuel):
    row, col = man
    time = 0
    visited = [[False]*N for _ in range(N)]
    visited[row][col] = True
    deq = deque()
    deq.append((row, col, time))

    if (row, col) in customer_destination:
        return (row, col), init_fuel - time

    while deq:
        row, col, time = deq.popleft()
        if (row, col) in customer_destination:
            return (row, col), init_fuel - time

        for w in range(4):
            
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == False and map_list[nr][nc] == 0:
                    if time + 1 > init_fuel:
                        continue
                    deq.append((nr, nc, time + 1))
                    visited[nr][nc] = True
    return (0,0) , -1

def take_cus(man):
    return (customer_destination[man][0], customer_destination[man][1])

def go_dest(man, destination, init_fuel):
    row, col = man
    time = 0
    visited = [[False]*N for _ in range(N)]
    visited[row][col] = True
    deq = deque()
    deq.append((row, col, time))

    while deq:
        row, col, time = deq.popleft()
        if (row, col) == destination:
            return (row, col), init_fuel + time

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == False and map_list[nr][nc] == 0:
                    if time + 1 > init_fuel:
                        continue
                    deq.append((nr, nc, time + 1))
                    visited[nr][nc] = True
    
    return (0, 0), -1
    

N, M, fuel = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(N)]
driver = list(map(lambda x: x-1, list(map(int,input().split()))))
customer_destination = {}

for _ in range(M):
    a = list(map(int,input().split()))
    customer_destination[(a[0]-1, a[1]-1)] = (a[2]-1, a[3]-1)

print(customer_destination)
for i in range(M):
    print('!!!',i+1)
    print(driver,fuel)
    next_cus, fuel = find_cus(driver, fuel)
    if fuel == -1:
        print(-1)
        break

    next_dest = take_cus(next_cus)
    print(next_cus,fuel)
    driver, fuel = go_dest(next_cus, next_dest, fuel)
    print(driver,fuel)
    if fuel == -1:
        print(-1)
        break

    
    del customer_destination[next_cus]

if fuel != -1:
    print(fuel)
