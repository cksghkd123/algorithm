from pprint import pprint


def check_ladder():
    for col in range(n):
        where = col
        for row in range(h):
            where += ladder_list[row][where]

        if where != col:
            return False
    else:
        return True

def play_ladder(row, col, result):
    global answer
    possible = check_ladder()
    if possible == True:
        answer = min(answer, result)
        return 
    
    if result == 3:
        return
    
    for nr in range(row, h):
        for nc in range(col, n-1):
            if ladder_list[nr][nc] == 0 and ladder_list[nr][nc+1] == 0:
                ladder_list[nr][nc] = 1
                ladder_list[nr][nc+1] = -1
                play_ladder(nr, nc, result+1)
                ladder_list[nr][nc]= 0
                ladder_list[nr][nc+1] = 0
        col = 0
    
n, m, h = map(int,input().split())
ladder_list = [[0]*n for _ in range(h)]

for _ in range(m):
    row, col = map(lambda x: int(x)-1,input().split())
    ladder_list[row][col] = 1
    ladder_list[row][col+1] = -1

answer = 4
play_ladder(0, 0, 0)
if answer == 4:
    print(-1)
else:
    print(answer)