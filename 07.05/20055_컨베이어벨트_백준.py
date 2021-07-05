import collections

N, K = map(int,input().split())
containerbelt = [0 for _ in range(2*N+1)]
durability = list(map(int,input().split()))
step = 0
robots = []

for _ in range(30):
    print('시작',containerbelt[0:2*N])
    step += 1
    #컨테이너 벨트 회전 + 내림
    if N-1 in robots:
        containerbelt[N-1] = 0
        robots.pop(robots.index(N-1))
    for i in range(len(containerbelt)-2,-1,-1):
        containerbelt[i+1] = containerbelt[i]
    containerbelt[0] = containerbelt[2*N]
    

    for i in range(len(robots)):
        if robots[i] < 2*N-1:
            robots[i] += 1
        else:
            robots[i] = 0

    print(containerbelt[0:2*N])
    #로봇 움직임
            
    print(robots)
    for i in range(len(robots)):
        if robots[i] == 2*N-1:
            if containerbelt[0] == 0 and durability[0] > 0:
                containerbelt[robots[i]] = 0
                containerbelt[0] = 1
                durability[0] -= 1
                robots[i] = 0

        elif containerbelt[robots[i]+1] == 0 and durability[robots[i]+1] > 0:
            containerbelt[robots[i]] = 0
            containerbelt[robots[i]+1] = 1
            durability[robots[i]+1] -= 1
            robots[i] += 1

    print(containerbelt[0:2*N])
    print(robots)
    #올림
    if containerbelt[0] == 0 and durability[0] > 0:
        containerbelt[0] = 1
        durability[0] -= 1
        robots.append(0)
    print(containerbelt[0:2*N])
    print(durability)
    #내구도 검사
    if durability.count(0) >= K:
        print(step)
        break

