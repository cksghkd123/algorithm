import collections
from pprint import pprint


n, m, k = map(int,input().split())
map_list = []
for _ in range(n):
    map_list.append(list(map(int,input().split())))


#BxC 에서 C를 score_guide에 미리 저장시켜준다.
map_trans = ((0,1),(1,0),(0,-1),(-1,0)) #우,하,좌,상
score_guide = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for row in range(n):
    for col in range(m):
        if visited[row][col]:
            continue
        
        ad_list = [(row,col)]
        visited[row][col] = True
        deq = collections.deque()
        deq.append((row,col))
        number = map_list[row][col]
        answer = 1

        while deq:
            x,y = deq.popleft()
            for i in range(4):
                new_x = x + map_trans[i][0]
                new_y = y + map_trans[i][1]

                if 0 <= new_x < n and 0 <= new_y < m:
                    if not visited[new_x][new_y]:
                        if map_list[new_x][new_y] == number:
                            visited[new_x][new_y] = True
                            deq.append((new_x,new_y))
                            answer += 1
                            ad_list.append((new_x,new_y))
        
        for x, y in ad_list:
            
            score_guide[x][y] = answer


#구현
dice_trans = [(3,2,0,1,4,5),(5,4,2,3,0,1),(2,3,1,0,4,5),(4,5,2,3,1,0)]

d = 0
dice = [1,6,3,4,5,2] # 위,아래,동,서,남,북
score = 0
row = 0
col = 0

for _ in range(k):
    if 0 > row+map_trans[d][0] or row+map_trans[d][0] >= n or 0 > col+map_trans[d][1] or col+map_trans[d][1] >=m:
        d += 2
        d %= 4
    row += map_trans[d][0]
    col += map_trans[d][1]
    
    new_dice = [dice[dice_trans[d][i]] for i in range(6)]
    dice = new_dice
    
    score += score_guide[row][col]*map_list[row][col]

    if dice[1] > map_list[row][col]:
        d += 1
        d %= 4
    elif dice[1] < map_list[row][col]:
        d -= 1
        d %= 4

print(score)


# 4 5 1000
# 4 1 2 3 3
# 6 1 1 3 3
# 5 6 1 3 2
# 5 5 6 5 5
#3901