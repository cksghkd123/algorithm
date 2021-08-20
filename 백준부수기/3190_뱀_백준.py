import collections


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def snake_game(row, col):
    count = 0
    direction = 0
    deq = collections.deque()
    deq.append((row,col))
    map_list[row][col] = 2

    while deq:
        tail_row, tail_col = deq.popleft()
        row = row + dr[direction]
        col = col + dc[direction] 
        count += 1
        if 0 <= row < n and 0 <= col < n and map_list[row][col] != 2:
            if map_list[row][col] == 1:
                deq.appendleft((tail_row, tail_col))
            elif map_list[row][col] == 0:
                map_list[tail_row][tail_col] = 0
            deq.append((row,col))
            map_list[row][col] = 2

            if count in snake_move:
                if snake_move[count] == 'L':
                    direction = (direction - 1)%4
                elif snake_move[count] == 'D':
                    direction = (direction + 1)%4
        else:
            return count

n = int(input())
k = int(input())
map_list = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    r, c = map(int,input().split())
    map_list[r-1][c-1] = 1
l = int(input())
snake_move = {}
for _ in range(l):
    a, b = input().split()
    snake_move[int(a)] = b

result = snake_game(0,0)
print(result)