def activate_rotate(gear_number, direction):
    if direction == 1:
        gears[gear_number] = [gears[gear_number][7]] + gears[gear_number][:7]
    elif direction == -1:
        gears[gear_number] = gears[gear_number][1:] + [gears[gear_number][0]]

def to_right(gear_number, direction):
    if gear_number+1 > 4:
        activate_rotate(gear_number, direction)
        return

    if gears[gear_number][2] == gears[gear_number+1][6]:
        activate_rotate(gear_number, direction)
    else:
        activate_rotate(gear_number, direction)
        to_right(gear_number+1, direction*-1)

def to_left(gear_number, direction):
    if gear_number-1 < 1:
        activate_rotate(gear_number, direction)
        return

    if gears[gear_number][6] == gears[gear_number-1][2]:
        activate_rotate(gear_number, direction)
    else:
        activate_rotate(gear_number, direction)
        to_left(gear_number-1, direction*-1)

def score():
    result = 0
    if gears[1][0] == 1:
        result += 1
    if gears[2][0] == 1:
        result += 2
    if gears[3][0] == 1:
        result += 4
    if gears[4][0] == 1:
        result += 8
    return result

gears = [[]]+[list(map(int,list(input()))) for _ in range(4)]
k = int(input())
rotate_list = [list(map(int,input().split())) for _ in range(k)]
#위 - 0 오 - 2 아 - 4 왼 - 6
for gear_number, direction in rotate_list:
    to_right(gear_number, direction)
    activate_rotate(gear_number, direction*-1)
    to_left(gear_number, direction)

answer = score()
print(answer)

