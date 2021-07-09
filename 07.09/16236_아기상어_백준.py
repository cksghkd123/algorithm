import collections


dr = [1,-1,0,0]
dc = [0,0,1,-1]

def findngo(sr,sc):
    arrive_time = []
    for t in food:
        tr = t[0]
        tc = t[1]
        visit = [[False for _ in range(N)] for _ in range(N)]
        deq = collections.deque()
        deq.append((0,sr,sc))

        while deq:
            time, row, col = deq.popleft()
            button = False

            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                
                if 0 <= nr < N and 0 <= nc < N:
                    if nr == tr and nc == tc:
                        time += 1
                        button = True
                        break

                    if visit[nr][nc] == False:
                        if map_list[nr][nc] <= shaq_size or map_list[nr][nc] == 9:
                            visit[nr][nc] = True
                            deq.append((time+1, nr, nc))
            
            if button == True:
                break
        
        arrive_time.append((time,tr,tc))
    
    if arrive_time == []:
        return True
    
    short = arrive_time[0]

    for i in range(1,len(arrive_time)):
        if short[0] > arrive_time[i][0]:
            short = arrive_time[i]

        elif short[0] == arrive_time[i][0]:
            if short[1] > arrive_time[i][1]:
                short = arrive_time[i]

            elif short[1] == arrive_time[i][1]:
                if short[2] < arrive_time[i][2]:
                    continue
                elif short[2] > arrive_time[i][2]:
                    short = arrive_time

    food.remove((short[1],short[2]))

    global mommy_time
    global ssr
    global ssc

    mommy_time += short[0]
    ssr = short[1]
    ssc = short[2]
    
    return False
        


N = int(input())
map_list = [list(map(int,input().split())) for _ in range(N)]
fish_list = {}
shaq_size = 2

for i in range(1,7):
    fish_list[i] = []


for row in range(N):
    for col in range(N):
        if 1 <= map_list[row][col] <= 6:
            fish_list[map_list[row][col]].append((row,col))
        elif map_list[row][col] == 9:
            ssr = row
            ssc = col


food = fish_list[1]
growth_count = 0
mommy_time = 0


while 1:
    bbutton = findngo(ssr,ssc)
    if bbutton == True:
        break

    growth_count += 1

    if growth_count == shaq_size:
        shaq_size += 1
        growth_count = 0
        if shaq_size<=7:
            food.extend(fish_list[shaq_size-1])

print(mommy_time)
    