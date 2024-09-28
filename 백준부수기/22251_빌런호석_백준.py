def dfs(curr, digit, count):
    print(curr, digit, count)
    result = 0
    if digit == 0:
        return result
    
    number = ( curr // digit ) % 10

    for i in range(10):
        add_count = bin(number_lights[number] ^ number_lights[i]).count('1')
        nxt = (curr // (digit * 10) * 10 + i) * digit + (curr % digit)
        
        if count + add_count <= P and nxt <= N:
            if i != number and nxt != 0:
                result += 1
            result += dfs(nxt, digit//10, count+add_count)
            
    return result

N, K, P, X = map(int, input().split())

number_lights = [
    0b1110111,
    0b0010010,
    0b1011101,
    0b1011011,
    0b0111010,
    0b1101011,
    0b1101111,
    0b1010010,
    0b1111111,
    0b1111011,
]

answer = dfs(X, P, 0)

print(answer)


