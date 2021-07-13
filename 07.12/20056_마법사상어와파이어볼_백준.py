import collections

def holjjak(x):
    if x/2 == x//2:
        return 0
    else:
        return 1

def fireball_move(row,col,mas,spd,dir,i):
    print('move')
    w = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
    nr, nc = (y + z for y,z in zip((row, col) , (map(lambda x: x*spd, w[dir]))))
    
    nr, nc = map(lambda x : x%N, (nr, nc))

    fireball_info[i][0] = nr
    fireball_info[i][1] = nc
    
    print(nr,nc)

    

def fireball_check():
    print('check')
    list = {}
    for i in range(len(fireball_info)):
        list[(fireball_info[i][0],fireball_info[i][1])] = []
    
    for i in range(len(fireball_info)):
        list[(fireball_info[i][0],fireball_info[i][1])].append(i)
    
    print(list)


    list2 = {}

    for key,val in list.items():
        if len(val) > 1:
            list2[key] = val
        
    return list2

def fireball_crash():
    print('crash')
    print(com_fireball,fireball_info)
    new_fireball_info = []
    for key, val in com_fireball.items():
        nd = None
        nm = 0
        ns = 0
        for n in val:
            print(fireball_info,n)
            nm += fireball_info[n][2]
            ns += fireball_info[n][3]
            if nd == None:
                hj = holjjak(fireball_info[n][4])
                nd = 0
            else:
                if nd == 0:
                    if holjjak(fireball_info[n][4]) != hj:
                        nd = 1
        
        nm = nm//5
        if nm == 0 :
            continue
        
        ns = ns//len(val)
        print(nm,ns,nd)


        if nd == 0:
            for i in range(4):
                new_fireball_info.append([key[0],key[1],nm,ns,i*2])
        elif nd == 1:
            for i in range(4):
                new_fireball_info.append([key[0],key[1],nm,ns,i*2+1])

    dellist = [d for d in i for i in com_fireball.values()]
    dellist.sort()
    for val in com_fireball.values():
        for n in reversed(dellist):
            fireball_info.pop(n)

    print(new_fireball_info)
    fireball_info.extend(new_fireball_info)
    
    print(fireball_info)

def fireball_mass():
    total = 0
    for n in fireball_info:
        total += n[2]
    print(total)
    
N, M, K = map(int,input().split())
fireball_info = [list(map(int,input().split())) for _ in range(M)]




for _ in range(K):
    i = 0
    for f in fireball_info:
        fireball_move(f[0],f[1],f[2],f[3],f[4],i)
        i += 1

    com_fireball = fireball_check()

    fireball_crash()

fireball_mass()





    
    