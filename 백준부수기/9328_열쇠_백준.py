import collections

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def solution(h, w, map_list, keys):
    result = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    doors = collections.defaultdict(list)
    keys_set = set(keys)
    deq = collections.deque()

    deq.append((0, 0))
    visited[0][0] = True

    while deq:
        cr, cc = deq.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                cell = map_list[nr][nc]

                if cell == '*':
                    continue

                visited[nr][nc] = True

                if cell == '$':
                    result += 1
                    deq.append((nr, nc))
                elif cell == '.':
                    deq.append((nr, nc))
                elif cell.isupper():
                    if cell.lower() in keys_set:
                        deq.append((nr, nc))
                    else:
                        doors[cell].append((nr, nc))
                elif cell.islower():
                    keys_set.add(cell)
                    deq.append((nr, nc))
                    if cell.upper() in doors:
                        for door_r, door_c in doors[cell.upper()]:
                            deq.append((door_r, door_c))

    return result

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    map_list = []
    map_list.append(['.' for _ in range(w + 2)])
    map_list.extend([['.'] + list(input()) + ['.'] for _ in range(h)])
    map_list.append(['.' for _ in range(w + 2)])

    keys = input().strip()
    if keys == '0':
        keys = ''

    answer = solution(h + 2, w + 2, map_list, keys)
    print(answer)
