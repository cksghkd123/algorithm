import collections
from pprint import pprint


complete = {1,2,3,4,5,6,7,8,9}
x = []
y = [set() for _ in range(9)]
squre = [set() for _ in range(9)]

unknown = collections.deque()
sudoku = []

for i in range(9):
    row = list(map(int,input().split()))
    sudoku.append(row)
    x.append(set(row))

    for j in range(9):
        if row[j] == 0:
            unknown.append((i, j))
        y[j].add(row[j])
        squre[(i//3)*3 + (j//3)].add(row[j])


n = 1
while unknown:
    print(unknown)
    pprint(sudoku)
    for _ in range(len(unknown)):
        i, j = unknown.popleft()
        k = (i//3)*3 + (j//3)
        temp = list(complete.difference(x[i]).intersection(complete.difference(y[j])).intersection(complete.difference(squre[k])))

        if len(temp) == n:
            gettin = temp.pop()
            sudoku[i][j] = gettin
            x[i].add(gettin)
            y[j].add(gettin)
            squre[k].add(gettin)
            n = 0
            break

        else:
            unknown.append((i, j))
    n += 1

for k in range(9):
    print(' '.join(map(str,sudoku[k])))

