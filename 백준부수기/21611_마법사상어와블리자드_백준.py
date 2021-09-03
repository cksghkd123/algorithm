import collections


def get_numbers(row, col):
    ddr = [0, 1, 0, -1]
    ddc = [-1, 0, 1, 0]
    w = 0
    index = 0
    for i in range(1, map_size):
        for _ in range(2):
            for _ in range(i):
                row += ddr[w]
                col += ddc[w]
                map_index[row][col] = index
                index += 1
                if map_list[row][col] != 0:
                    numbers.append(map_list[row][col])
            w = (w+1)%4

    for _ in range(map_size-1):
        row += ddr[w]
        col += ddc[w]
        map_index[row][col] = index
        index += 1
        if map_list[row][col] != 0:
            numbers.append(map_list[row][col])
    

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def blizard(row, col, direction, long):
    delete_list = []
    for l in range(1, long+1):
        delete_list.append(map_index[row + l*dr[direction]][col + l*dc[direction]])
    r = len(numbers)
    index = 0
    for _ in range(r):

        number = numbers.popleft()
        if index in delete_list:
            index += 1
            continue
        else:
            numbers.append((number))
            index += 1

def bomb(numbers:collections.deque):
    score = 0
    r = len(numbers)
    temp_deq = collections.deque()
    bomb_number = 0
    for _ in range(r):
        number = numbers.popleft()
        if number != bomb_number:
            if len(temp_deq) >= 4:
                while temp_deq:
                    nnumber = temp_deq.popleft()
                    score += nnumber
            else:
                while temp_deq:
                    nnumber = temp_deq.popleft()
                    numbers.append(nnumber)
            bomb_number = number
            temp_deq.append(number)
        elif number == bomb_number:
            temp_deq.append(number)

    if len(temp_deq) >= 4:
        while temp_deq:
            number = temp_deq.popleft()
            score += number
    else:
        while temp_deq:
            number = temp_deq.popleft()
            numbers.append(number)

    return score

def transforming(numbers:collections.deque):
    if len(numbers) == 0 :
        return
    marble_number = numbers.popleft()
    temp_count = 1
    r = len(numbers)
    for _ in range(r):
        number = numbers.popleft()
        if number != marble_number:
            numbers.append(temp_count)
            numbers.append(marble_number)
            marble_number = number
            temp_count = 1
        elif number == marble_number:
            temp_count += 1
    
    numbers.append(temp_count)
    numbers.append(marble_number)
    while len(numbers) > map_size**2 -1:
        numbers.pop()

map_size, spell_count = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(map_size)]
map_index = [[0 for _ in range(map_size)] for _ in range(map_size)]
spells = [list(map(int,input().split())) for _ in range(spell_count)]
shq = (map_size//2, map_size//2)
numbers = collections.deque()
get_numbers(*shq)

score = 0
for direction, long in spells:
    blizard(*shq, direction, long)
    combo_bomb = True
    while combo_bomb:
        get_score = bomb(numbers)
        score += get_score
        if get_score == 0:
            combo_bomb = False
    transforming(numbers)

print(score)
