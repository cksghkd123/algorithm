from collections import deque


w = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(places, room, person_list):

    for row, col in person_list:
        deq = deque()
        visit = [[False] * 5 for _ in range(5)]
        visit[row][col] = True
        i = 0
        deq.append((row,col,i))
    
        while deq:

            row, col, dis = deq.popleft()
            if dis == 2:
                break

            for dw in range(4):
                nr, nc = (row + w[dw][0], col + w[dw][1]) 

                if 0 <= nr < 5 and 0 <= nc < 5:
                    if visit[nr][nc] == False:
                        if places[room][nr][nc] == 'P':
                            return 0
                        elif places[room][nr][nc] == 'O':
                            visit[nr][nc] = True
                            deq.append((nr,nc,dis+1))
                        
    return 1
            

def solution(places):
    answer = []
    
    for room in places:
        for i in range(len(room)):
            room[i] = list(room[i])
    
    for room in range(5):
        people = []
        for row in range(5):
            for col in range(5):
                if places[room][row][col] == 'P':
                    people.append((row,col))
        answer.append(bfs(places,room,people))
    
    return answer