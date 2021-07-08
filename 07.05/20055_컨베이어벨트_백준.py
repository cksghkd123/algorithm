import collections

N, K = map(int,input().split())
containerbelt = [[n,0] for n in range(2*N+1)]
durability = list(map(int,input().split()))
step = 0


while 1:
    step += 1
    #컨테이너 벨트 회전
    
    for i in range(len(containerbelt)-2,-1,-1):
        containerbelt[i+1] = containerbelt[i]
    containerbelt[0] = containerbelt[2*N]

    if containerbelt[N-1][1] == 1:
        containerbelt[N-1][1] = 0

    #로봇 움직임
            
    for i in range(N-1,-1,-1) :
        if containerbelt[i][1] == 1 and containerbelt[i+1][1] == 0 and durability[containerbelt[i+1][0]] > 0:
            containerbelt[i][1], containerbelt[i+1][1] = 0,1
            durability[containerbelt[i+1][0]] -= 1
    if containerbelt[N-1][1] == 1:
        containerbelt[N-1][1] = 0

    #올림
    if containerbelt[0][1] == 0 and durability[containerbelt[0][0]] > 0:
        containerbelt[0][1] = 1
        durability[containerbelt[0][0]] -= 1
        

    #내구도 검사
    if durability.count(0) >= K:
        print(step)
        break