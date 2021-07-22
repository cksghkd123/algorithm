from pprint import pprint
def queen(row,col):
    
    chessboard[row][col] = 1
    que.append((row,col))
    rque.append(row)


    if len(que) == N:
        global count
        count += 1
        que.pop()
        rque.pop()
        return

    
    
    for w in range(N):
        
        if w in rque:
            continue
        nr = w
        break
        
    for nc in range(N):
        BREAK = False
        Button = False
        for w in range(len(que)):
            if nc == que[w][1]-abs(que[w][0]-nr) or nc == que[w][1]+abs(que[w][0]-nr) or nc == que[w][1]: 
                BREAK = True
                break
        if BREAK == True:
            if nc == N-1:
                rque.pop()
                que.pop()
                return
            continue
        queen(nr,nc)
            
    
    rque.pop()
    que.pop()
    return

    
    
N = int(input())
count = 0


for row in range(N):
    chessboard = [[0 for _ in range(N)] for _ in range(N)]
    que = []
    rque = []
    queen(row,0)

print(count)
