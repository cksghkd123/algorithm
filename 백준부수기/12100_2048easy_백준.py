from copy import deepcopy


def combination(list, r, result, last):
    if len(result) == r:
        com.append(result)
        return
    
    for dir in list:
        combination(list, r, result + [dir], dir)

def play_2048(list, case):
    for i in case:
        if i == 'left':
            for row in range(n):
                puzzle = 0
                index = 0
                for col in range(n):
                    if list[row][col] != 0:
                        if puzzle == 0:
                            puzzle = list[row][col]
                        elif list[row][col] != puzzle:
                            list[row][index] = puzzle
                            puzzle = list[row][col]
                            index += 1
                        else:
                            list[row][index] = 2*puzzle
                            puzzle = 0
                            index += 1
                list[row][index] = puzzle
                for col in range(index+1, n):
                    list[row][col] = 0

        elif i == 'right':
            for row in range(n):
                puzzle = 0
                index = n-1
                for col in range(n-1,-1,-1):
                    if list[row][col] != 0:
                        if puzzle == 0:
                            puzzle = list[row][col]
                        elif list[row][col] != puzzle:
                            list[row][index] = puzzle
                            puzzle = list[row][col]
                            index -= 1
                        else:
                            list[row][index] = 2*puzzle
                            puzzle = 0
                            index -= 1
                list[row][index] = puzzle
                for col in range(index-1,-1,-1):
                    list[row][col] = 0
        elif i == 'up':
            for col in range(n):
                puzzle = 0
                index = 0
                for row in range(n):
                    if list[row][col] != 0:
                        if puzzle == 0:
                            puzzle = list[row][col]
                        elif list[row][col] != puzzle:
                            list[index][col] = puzzle
                            puzzle = list[row][col]
                            index += 1
                        else:
                            list[index][col] = 2*puzzle
                            puzzle = 0
                            index += 1
                list[index][col] = puzzle
                for row in range(index+1, n):
                    list[row][col] = 0

        elif i == 'down':
            for col in range(n):
                puzzle = 0
                index = n-1
                for row in range(n-1,-1,-1):
                    if list[row][col] != 0:
                        if puzzle == 0:
                            puzzle = list[row][col]
                        elif list[row][col] != puzzle:
                            list[index][col] = puzzle
                            puzzle = list[row][col]
                            index -= 1
                        else:
                            list[index][col] = 2*puzzle
                            puzzle = 0
                            index -= 1
                list[index][col] = puzzle
                for row in range(index-1,-1,-1):
                    list[row][col] = 0

        result = 0
    
    for i in list:
        result = max(result, max(i))

    return result

n = int(input())
board_list = [list(map(int,input().split())) for _ in range(n)]

direction = ['left', 'right', 'up', 'down']
result = 0
com = []
combination(direction, 5, [], None)
for c in com:
    new_board = deepcopy(board_list)
    n_result = play_2048(new_board, c)
    result = max(n_result, result)

print(result)