N, d, k, c = map(int, input().split())

sushi_list = [int(input()) for _ in range(N)]

answer = 0
count = 1
dishes = {c: 1}

for i in range(N+k):
    if i >= k:
        dishes[sushi_list[i-k]] -= 1
        if dishes[sushi_list[i-k]] == 0:
            count -= 1
    
    if sushi_list[i%N] not in dishes:
        dishes[sushi_list[i%N]] = 1
    else:
        dishes[sushi_list[i%N]] += 1
    
    if dishes[sushi_list[i%N]] == 1:
        count += 1
        answer = max(answer, count)
    
print(answer)