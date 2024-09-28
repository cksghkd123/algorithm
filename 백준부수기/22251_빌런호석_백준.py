def cost_to_change(a, b):
    result = 0
    for i in range(7):        
        if number_lights[a][i] != number_lights[b][i]:
            result += 1

    return result

def dfs(curr, digit, count):
    result = 0
    if curr > N:
        return 0
    
    if digit == K:
        if curr != 0 and curr != X:
            return 1

        return 0

    for i in range(10):
        add_count = cost_to_change(number_by_digit[digit], i)
        nxt = curr + i*(10**digit)
        if count + add_count <= P and nxt <= N:
            result += dfs(nxt, digit+1, count+add_count)
            
    return result

N, K, P, X = map(int, input().split())

number_lights = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
    ]

number_by_digit = []
temp = X

for _ in range(K):
    number_by_digit.append(temp%10)
    temp //= 10
    
answer = dfs(0, 0, 0)

print(answer)


