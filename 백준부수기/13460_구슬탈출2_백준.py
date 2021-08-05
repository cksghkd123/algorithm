import collections
from pprint import pprint

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def which_first(ddr, ddc, red_row, red_col, blue_row, blue_col):
    temp = (ddr, ddc)
    if temp == (0, 1):
        if blue_col > red_col:
            return 'Blue'
        else:
            return 'Red'
    elif temp == (0, -1):
        if blue_col < red_col:
            return 'Blue'
        else:
            return 'Red'
    elif temp == (1, 0):
        if blue_row > red_row:
            return 'Blue'
        else:
            return 'Red'
    elif temp == (-1, 0):
        if blue_row < red_row:
            return 'Blue'
        else:
            return 'Red'

def straight(ddr, ddc, row, col):
    while map_list[row][col] != '#' :
        row += ddr
        col += ddc
        if map_list[row][col] == 'O':
            return row, col
    
    row -= ddr
    col -= ddc

    return row, col

def bfs(red, blue):
    visited[red[0]][red[1]].append(blue)
    deq = collections.deque()
    deq.append((0, *red, *blue))

    while deq:
        count, rrow, rcol, brow, bcol = deq.popleft()
        for w in range(4):
            first = which_first(dr[w], dc[w], rrow, rcol, brow, bcol)
            if first == 'Red':
                nrr, nrc = straight(dr[w], dc[w], rrow, rcol)
                nbr, nbc = straight(dr[w], dc[w], brow, bcol)

                if map_list[nbr][nbc] == 'O':
                    continue

                if map_list[nrr][nrc] == 'O':
                    return count+1
                
                if (nrr, nrc) == (nbr, nbc):
                    nbr -= dr[w]
                    nbc -= dc[w]

                if (nbr, nbc) not in visited[nrr][nrc]:
                    visited[nrr][nrc].append((nbr, nbc))
                    deq.append((count+1, nrr, nrc , nbr, nbc))

            elif first == 'Blue':
                nrr, nrc = straight(dr[w], dc[w], rrow, rcol)
                nbr, nbc = straight(dr[w], dc[w], brow, bcol)

                if map_list[nbr][nbc] == 'O':
                    continue
                
                if map_list[nrr][nrc] == 'O':
                    return count+1

                if (nrr, nrc) == (nbr, nbc):
                    nrr -= dr[w]
                    nrc -= dc[w]

                if (nbr, nbc) not in visited[nrr][nrc]:
                    visited[nrr][nrc].append((nbr, nbc))
                    deq.append((count+1, nrr, nrc , nbr, nbc))
                
    return -1


n, m = map(int,input().split())
map_list = [list(input()) for _ in range(n)]
marble_info = collections.defaultdict(list)
for row in range(n):
    for col in range(m):
        if map_list[row][col] != '#':
            marble_info[map_list[row][col]].append((row, col))

visited = [[[] for _ in range(m)] for _ in range(n)]


result = bfs(marble_info['R'][0], marble_info['B'][0])
if result <= 10:
    print(result)
else:
    print(-1)
