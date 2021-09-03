from copy import deepcopy
from collections import deque

def move_cloud(direction, long, clouds):
    r = len(clouds)
    for _ in range(r):
        row, col = clouds.popleft()
        row = (row + (long * dr[direction])) % map_size
        col = (col + (long * dc[direction])) % map_size
        clouds.append((row, col))


def raining(clouds):
    exhaused_clouds = []
    while clouds:
        row, col = clouds.popleft()
        map_list[row][col] += 1
        exhaused_clouds.append((row, col))
    
    return exhaused_clouds

def water_copy(exhaused_clouds):
    for row, col in exhaused_clouds:
        count = 0
        for w in range(2, 9, 2):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < map_size and 0 <= nc < map_size:
                if map_list[nr][nc] != 0:
                    count += 1
        map_list[row][col] += count

def making_cloud(exhaused_clouds):
    for row in range(map_size):
        for col in range(map_size):
            if map_list[row][col] >= 2:
                if (row, col) in exhaused_clouds:
                    continue
                else:
                    clouds.append((row, col))
                    map_list[row][col] -= 2

def checking():
    result = 0
    for row in range(map_size):
        for col in range(map_size):
            result += map_list[row][col]

    return result

map_size, movement_count = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(map_size)]
movements = [list(map(int,input().split())) for _ in range(movement_count)]
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(map_size-1, 0), (map_size-1, 1), (map_size-2, 0), (map_size-2, 1)]
clouds = deque(clouds)

for move in movements:
    direction, long = move
    move_cloud(direction, long, clouds)
    exhaused_clouds = raining(clouds)
    water_copy(exhaused_clouds)
    making_cloud(exhaused_clouds)

answer = checking()
print(answer)