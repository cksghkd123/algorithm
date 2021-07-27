from collections import defaultdict


def security_straight(directions, camera_row, camera_col):
    result = set()

    for d in directions:
        nr = camera_row + d[0]
        nc = camera_col + d[1]

        while 0 <= nr < n and 0 <= nc < m:
            if (nr, nc) in items[6]:
                break
            if (nr, nc) in items[0]:
                result.add((nr, nc))

            nc += d[1]
            nr += d[0]

    return result

def at_product(num, camera_row, camera_col):
    result = []

    if num == 1:
        directions = ( [(1,0)], [(-1,0)], [(0,1)], [(0,-1)] )
    
    elif num == 2:
        directions = ( ((1,0), (-1,0)), ((0,1), (0,-1)) )

    elif num == 3:
        directions = ( ((1,0), (0,1)), ((1,0), (0,-1)), ((-1,0),(0,1)), ((-1,0),(0,-1)))

    elif num == 4:
        directions = ( ((-1,0), (0,1), (0,-1)), ((1,0), (0,1), (0,-1)), ((1,0), (-1,0), (0,-1)), ((1,0), (-1,0), (0,1)) )

    elif num == 5:
        directions = [ ((1,0), (-1,0), (0,1), (0,-1)) ]

    for ds in directions:
        case = security_straight(ds, camera_row, camera_col)
        if not case:
            continue
        result.append(case)

    return result

def case_list(select):
    result = []

    for i in range(1,6):
        for row, col in select[i]:
            case = at_product(i, row, col)
            if not case:
                continue
            result.append(case)
    
    return result

def security_zone(camera_num, case_num, result, ccase_list):
    new_camera_n = camera_num + 1

    global a
    if new_camera_n == len(ccase_list):
        a.append(len(result))
        return

    for new_case_n in range(len(ccase_list[new_camera_n])):
        security_zone(new_camera_n, new_case_n, result.union(ccase_list[new_camera_n][new_case_n]), ccase_list)


n, m = map(int,input().split())

items = defaultdict(list)
for row in range(n):
    map_list = list(map(int,input().split()))
    for col in range(m):
        items[map_list[col]].append((row, col))


com = case_list(items)
empty_room = len(items[0])

if com != []:
    empty_set = set()
    a = []
    for new_case_n in range(len(com[0])):
        security_zone(0, new_case_n, empty_set.union(com[0][new_case_n]), com)

    answer = empty_room - max(a)
    print(answer)


else:
    print(empty_room)
