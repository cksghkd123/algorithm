dr = [0,0,1,-1]
dc = [1,-1,0,0]

def select1(num):
    global N
    max_like = []

    for row in range(N):
        for col in range(N):
            like_count = 0
            if shqclass[row][col] != 0:
                continue
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]

                if 0 <= nr < N and 0 <= nc < N:
                    if shqclass[nr][nc] in student_like[num]:
                        like_count += 1
            if max_like == [] or max_like[0][0] == like_count:
                max_like.append((like_count,row,col))
            elif max_like[0][0] > like_count:
                continue
            elif max_like[0][0] < like_count:
                max_like = []
                max_like.append((like_count,row,col))
    if len(max_like) > 1:
        select2(student_like[num][0],max_like)                       
    else:
        shqclass[max_like[0][1]][max_like[0][2]] = student_like[num][0]


def select2(stu,like):
    global N
    max_no = []

    for i in range(len(like)):
        row = like[i][1]
        col = like[i][2]
        no_count = 0

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if shqclass[nr][nc] == 0:
                    no_count += 1
        if max_no == [] or max_no[0][0] == no_count:
            max_no.append((no_count,row,col))
        elif max_no[0][0] > no_count:
            continue
        elif max_no[0][0] < no_count:
            max_no = []
            max_no.append((no_count,row,col))
    
    if len(max_no) > 1:
        select3(stu, max_no)
    else:
        shqclass[max_no[0][1]][max_no[0][2]] = stu

def select3(stu,list):
    shqclass[list[0][1]][list[0][2]] = stu

def likelike(num,row,col):
    global N
    global result

    for i in range(N**2):
        if student_like[i][0] == num:
            like = [student_like[i][n] for n in range(1,5)]
            break
    
    likecount = 0 

    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]

        if 0 <= nr < N and 0 <= nc < N:
            if shqclass[nr][nc] in like:
                likecount += 1

    if likecount > 0:
        result += 10**(likecount-1)


N = int(input())
student_like = [list( map(int,input().split())) for _ in range(N**2)]
shqclass = [[0 for _ in range(N)] for _ in range(N)]

for num in range(len(student_like)):
    select1(num)

result = 0
for row in range(N):
    for col in range(N):
        likelike(shqclass[row][col],row,col)

print(result)
