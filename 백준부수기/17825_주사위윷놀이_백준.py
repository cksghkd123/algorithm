def go_yut(where, dice):
    if where == 35:
        return 35, 0
    
    if dice != 0:
        return go_yut(yut_table[where][2], dice-1)
        
    else:
        if where == 5:
            return 21, 10
        elif where == 10:
            return 25, 20
        elif where == 15:
            return 28, 30

        return where, yut_table[where][1]
    

def play_yut(member, time, total_score):
    if time == len(dice_sequence):
        global result
        result = max(result, total_score)
        return

    for m in range(len(member)):
        if member[m] < 35:
            nextwhere, score = go_yut(member[m], dice_sequence[time])
            if nextwhere == 35:
                yut_table[member[m]][3] = False
                temp = member[m]
                member[m] = nextwhere
                play_yut(member, time+1, total_score+score)
                member[m] = temp
                yut_table[member[m]][3] = True
                
            elif yut_table[nextwhere][3] == False:
                yut_table[member[m]][3] = False
                yut_table[nextwhere][3] = True
                temp = member[m]
                member[m] = nextwhere
                play_yut(member, time+1, total_score+score)
                member[m] = temp
                yut_table[nextwhere][3] = False
                yut_table[member[m]][3] = True

    if len(member) < 4:
        nextwhere, score = go_yut(0, dice_sequence[time])
        if yut_table[nextwhere][3] == False:
            yut_table[nextwhere][3] = True
            play_yut(member+[nextwhere], time+1, total_score+score)
            yut_table[nextwhere][3] = False
        

dice_sequence = list(map(int,input().split()))
yut_table = [[0,0,1]] + [[i,2*i,i+1,False] for i in range(1,20)] + [[20,40,35,False]] + [[i+21, 3*i+10, i+22, False] for i in range(4)] + [[i+25, 2*i+20, i+26, False] for i in range(3)] + [[28, 30, 29, False]] + [[i+29, 28-i, i+30, False] for i in range(4)] + [[33, 30, 34, False]] + [[34, 35, 20, False]] + [[35, []]]
yut_table[24][2] = 32
yut_table[27][2] = 32
result = 0
play_yut([], 0, 0)
print(result)
