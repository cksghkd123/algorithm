import collections
from pprint import pprint

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def combination(i, target, k, result):

    if len(result) == target:
        return [result]

    if i == k:
        return []

    return combination(i+1, target, k, result + [i]) + combination(i+1, target, k, result)

n, m = map(int, input().split())
answer = -1
laboratory =[list(map(int, input().split())) for _ in range(n)]

virus_point_list = []
target_count = 0
for row in range(n):
    for col in range(n):
        if laboratory[row][col] == 2:
            virus_point_list.append((row, col))
        if laboratory[row][col] == 0:
            target_count += 1
# print(virus_point_list)

comb_list = combination(0,  m, len(virus_point_list), [])

for comb_element in comb_list:
    deq = collections.deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in comb_element:
        deq.append(virus_point_list[i])
        visited[virus_point_list[i][0]][virus_point_list[i][1]] = 0
    
    result = -1
    checked_count = 0
    time = 0
    while deq:
        cr, cc = deq.popleft()
        if laboratory[cr][cc] == 0:
            time = visited[cr][cc]
        
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                if laboratory[nr][nc] == 0:
                    visited[nr][nc] = visited[cr][cc] + 1
                    checked_count += 1
                    deq.append((nr, nc))
                elif laboratory[nr][nc] == 2:
                    visited[nr][nc] = visited[cr][cc] + 1
                    deq.append((nr, nc))

    if checked_count == target_count:
        result = time

    # print(checked_count, target_count)
    # print(visited)
    if result == -1:
        continue

    if answer == -1:
        answer = result
    elif result < answer:
        answer = result

    # print(f"comb_element: {comb_element}")
    # print(f"answer = {answer}, result = {result}")
print(answer)

