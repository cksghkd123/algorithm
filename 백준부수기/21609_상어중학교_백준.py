import collections


dr = [1, -1, 0 ,0]
dc = [0, 0, 1, -1]
def biggest_group():
    the_biggest = [0]
    visited = [[False for _ in range(table_size)] for _ in range(table_size)]
    for row in range(table_size):
        for col in range(table_size):
            if visited[row][col] == False and table_list[row][col] > 0:
                visited[row][col] = True
                group = searching_group(row, col, table_list[row][col], visited)
                if len(the_biggest) < len(group):
                    the_biggest = group
                elif len(the_biggest) == len(group):
                    if the_biggest[-1] < group[-1]:
                        the_biggest = group
                    elif the_biggest[-1] == group[-1]:
                        the_biggest = group
    the_biggest.pop()
    return the_biggest

def searching_group(row, col, color, visited):
    deq = collections.deque()
    deq.append((row, col))
    rainbow_list = []
    result_list = [(row, col)]
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < table_size and 0 <= nc < table_size:
                if visited[nr][nc] == False:
                    if table_list[nr][nc] == color or table_list[nr][nc] == 0:
                        visited[nr][nc] = True
                        deq.append((nr, nc))
                        result_list.append((nr, nc))
                        if table_list[nr][nc] == 0:
                            rainbow_list.append((nr, nc))
    
    if len(result_list) < 2:
        return [0]

    result_list.append(len(rainbow_list))

    for row, col in rainbow_list:
        visited[row][col] = False
    
    return result_list

def get_score(the_big):
    score = len(the_big)**2
    for row, col in the_big:
        table_list[row][col] = -2
    return score

def gravity():
    for col in range(table_size):
        for row in range(table_size-1, -1, -1):
            if table_list[row][col] == -1 or table_list[row][col] == -2:
                continue
            color = table_list[row][col]
            table_list[row][col] = -2
            nr = row
            nr += 1
            while nr < table_size and table_list[nr][col] == -2:
                nr += 1
            nr -= 1
            table_list[nr][col] = color

def rotate():
    rotated_list = [[-2 for _ in range(table_size)] for _ in range(table_size)]
    for row in range(table_size):
        for col in range(table_size):
            rotated_list[table_size-1-col][row] = table_list[row][col]
    
    return rotated_list

table_size, color_count = map(int,input().split())
table_list = [list(map(int,input().split())) for _ in range(table_size)] 
score = 0
the_big = biggest_group()
while len(the_big) > 1:
    score += get_score(the_big)
    gravity()
    table_list = rotate()
    gravity()
    the_big = biggest_group()
print(score)