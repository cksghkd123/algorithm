numTest = int(input())

for i in range(numTest):        
    c = list(map(int,input().split()))
    
    distance = (((c[0]-c[3])**2) + ((c[1]-c[4])**2))**(1/2)
    radius = c[2] + c[5]
    radius_dif = abs(c[2]-c[5])


    #두 원"의 중심"이 정확히 겹칠경우
    #"r1 == r2" => -1
    if c[0] == c[3] and c[1] == c[4]:
        if c[2] == c[5]:
            possoble_coordinate = -1
    #"else" => 0
        else:
            possoble_coordinate = 0

    #"아닐 경우"
    else:
    #"r1+r2 < d" => 0
        if distance > radius:
            possoble_coordinate = 0
    #"abs(r1-r2) (절대값) == d" => 1
        elif radius_dif == distance:
            possoble_coordinate = 1
    #"abs(r1-r2) > d" => 0
        elif radius_dif > distance:
            possoble_coordinate = 0
    #"r1+r2 == d" => 1
        elif distance == radius:
            possoble_coordinate = 1
    #"r1+r2 > d" => 2
        elif distance < radius:
            possoble_coordinate = 2
        
    print(possoble_coordinate)

