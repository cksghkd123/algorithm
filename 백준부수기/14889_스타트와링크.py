def combination(number, k, target, result):
    if len(result) == target:
        cases.append(result)
        return
    
    if k == number:
        return
    
    combination(number, k+1, target, result + [k])
    combination(number, k+1, target, result)

def permutation(array, target, result):
    if len(result) == target:
        global team_swich
        if team_swich == True:
            global start_team
            start_team += ability_table[result[0]][result[1]]
        else:
            global link_team
            link_team += ability_table[result[0]][result[1]]
        return

    for i in range(len(array)):
        if p_visited[i] == False:
            p_visited[i] = True
            permutation(array, target, result + [array[i]])
            p_visited[i] = False

n = int(input())
ability_table = [list(map(int,input().split())) for _ in range(n)]
total = sum(sum(ability_table[i]) for i in range(n))

cases = []
combination(n, 0, n//2, [])

result = float('inf')
for c in range(len(cases)//2):
    p_visited = [False for _ in range(len(cases[c]))]
    start_team = 0
    link_team = 0
    team_swich = True
    permutation(cases[c], 2, [])
    team_swich = False
    permutation(cases[len(cases)-1-c], 2, [])
    result = min(result, abs(start_team - link_team))

print(result)