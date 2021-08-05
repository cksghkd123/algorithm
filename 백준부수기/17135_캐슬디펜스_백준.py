from pprint import pprint
import collections
from copy import deepcopy


dr = [0, -1, 0]
dc = [-1, 0, 1]
def arrow_attack(castle, row, col, k):
    deq = collections.deque()
    deq.append((row,col,k))
    if castle[row][col] == 1:
        return (row,col)
    visited = []
    visited.append((row,col))

    while deq:
        row, col, kk = deq.popleft()
        if kk > 0:
            for w in range(3):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < n and 0 <= nc < m:
                    if (nr,nc) not in visited:
                        if castle[nr][nc] == 1:
                            return (nr,nc)
                        visited.append((nr,nc))
                        deq.append((nr, nc, kk-1))


def castle_defence(castle, attack_range):
    count = 0
    kill_list = set()
    for col in range(m):
        if castle[n][col] == 2:
            kill = arrow_attack(castle, n-1, col, attack_range-1)
            if kill != None:
                kill_list.add(kill)
    for row, col in kill_list:
        castle[row][col] = 0
        count += 1
    
    return count


def castle_attack(castle, index):
    after_move = [[0 for _ in range(m)]] + castle[:n-1] + [castle[-1]]
    return after_move


def combination(length, k, r, t, result):
    if t > r:
        return
    if k >= length:
        if t == r:
            com.append(result)
        return
    else:
        combination(length, k+1, r, t+1, result+[2])
        combination(length, k+1, r, t, result+[0])


n, m, d = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(n)] + [[0 for _ in range(m)]]

com = []
combination(m,0,3,0,[])
result = 0

for case in com:
    new_map_list = deepcopy(map_list)
    new_map_list[n] = case
    n_result = 0
    for k in range(1, n+1):
        n_result += castle_defence(new_map_list, d)
        new_map_list = castle_attack(new_map_list, k)
    result = max(result, n_result)

print(result)