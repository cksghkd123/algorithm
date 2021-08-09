import collections


dr = (-1, 0, 0, 1)
dc = (0, -1, 1, 0)
def find_customer(texi_row, texi_col, k):
    visited[texi_row][texi_col][k] = True
    deq = collections.deque()
    deq.append((texi_row, texi_col, 0))
    candidate = []

    while deq:
        row, col, count  = deq.popleft()
        if candidate:
            if count > max_count:
                continue
        for i in range(len(customer_destination)):
            if row == customer_destination[i][0] and col == customer_destination[i][1]:
                a, b, c, d = customer_destination[i]
                max_count = count
                candidate.append((a,b,c,d,i))
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < n:
                if map_list[nr][nc] == 0 and visited[nr][nc][k] == False:
                    visited[nr][nc][k] = True
                    deq.append((nr,nc,count+1))
    
    if candidate:
        candidate.sort()
        a, b, c, d, i = candidate[0]
        customer_destination.pop(i)
        return max_count, a, b, c, d

    return None, None, None, None, None

def go_destination(texi_row, texi_col, dest_row, dest_col ,k):
    visited[texi_row][texi_col][k] = True
    deq = collections.deque()
    deq.append((texi_row, texi_col, 0))

    while deq:
        row, col, count  = deq.popleft()
        if row == dest_row and col == dest_col:
            return count, row, col
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < n and 0 <= nc < n:
                if map_list[nr][nc] == 0 and visited[nr][nc][k] == False:
                    visited[nr][nc][k] = True
                    deq.append((nr,nc,count+1))

    return None, None, None

n, m, fuel = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)]
t_r, t_c = map(lambda x: int(x)-1,input().split())
customer_destination = [list(map(lambda x: int(x)-1,input().split())) for _ in range(m)]
visited = [[[False for _ in range(2*m)] for _ in range(n)] for _ in range(n)]
visited_index = 0

while customer_destination:
    required_fuel, c_r, c_c, d_r, d_c = find_customer(t_r, t_c, visited_index)
    #벽에 막혔을 때
    if required_fuel == None:
        print(-1)
        break
    visited_index += 1
    fuel -= required_fuel
    #연료가 다 떨어졌을 때
    if fuel < 0:
        print(-1)
        break

    required_fuel, t_r, t_c = go_destination(c_r, c_c, d_r, d_c, visited_index)
    #벽에 막혔을 때
    if required_fuel == None:
        print(-1)
        break
    visited_index += 1
    fuel -= required_fuel
    #연료가 다 떨어졌을 때
    if fuel < 0:
        print(-1)
        break
    fuel += required_fuel*2

    if visited_index == m*2:
        print(fuel)