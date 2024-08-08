N = int(input())

map_list = [list(map(int, input().split())) for _ in range(N)]

que = []
que.append((0, 1, 0))

directions = [[(0, 1, 0), (1, 1, 2)], [(1, 0, 1), (1, 1, 2)], [(0, 1, 0), (1, 0, 1), (1, 1, 2)]]
banned = [[(0, 1)], [(1, 0)], [(0, 1), (1, 0), (1,1)]]

answer = 0
if  map_list[N-1][N-1] != 1:
    while que:
        r, c, s =  que.pop()
        if r == N-1 and c == N-1:
            answer += 1
            continue

        for dr, dc, ns in directions[s]:
            nr = r + dr
            nc = c + dc

            if nr < N and nc < N:
                for ddr, ddc in banned[ns]:
                    br = r + ddr
                    bc = c + ddc

                    if br < N and bc < N:
                        if map_list[br][bc] == 1:
                            break
                else:
                    que.append((nr, nc, ns))        

print(answer)