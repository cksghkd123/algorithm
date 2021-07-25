from collections import *


def make_it(row, col, num):
    x[row].remove(num)
    y[col].remove(num)
    squre[3*(row//3) + (col//3)].remove(num)
    sudoku[row][col] = num

def return_it(row, col, num):
    x[row].add(num)
    y[col].add(num)
    squre[3*(row//3) + (col//3)].add(num)
    sudoku[row][col] = 0

def solve_sudoku(index):
    global button
    if button:
        return

    if index == len(spots):
        for i in range(9):
            print(' '.join(map(str,sudoku[i])))
        button = True
        return
    
    row, col = spots[index]

    possible = x[row] & y[col] & squre[3*(row//3) + (col//3)]

    if len(possible) == 0:
        return

    if len(possible) == 1:
        make_it(row, col, list(possible)[0])
        solve_sudoku(index + 1)
        return_it(row, col, list(possible)[0])
        
    else:
        for i in possible:
            make_it(row, col, i)
            solve_sudoku(index + 1)
            return_it(row, col ,i)

    return

        
sudoku = []
x = [{i+1 for i in range(9)} for _ in range(9)]
y = [{i+1 for i in range(9)} for _ in range(9)]
squre = [{i+1 for i in range(9)} for _ in range(9)]
spots = deque()

for row in range(9):
    sudoku.append(list(map(int,input().split())))
    x[row] = x[row].difference(set(sudoku[row]))
    for col in range(9):
        if sudoku[row][col] == 0:
            spots.append((row, col))
            continue
        part = 3*(row//3) + (col//3)
        y[col] = y[col].difference({sudoku[row][col]})
        squre[part] = squre[part].difference({sudoku[row][col]})

button = False
solve_sudoku(0)