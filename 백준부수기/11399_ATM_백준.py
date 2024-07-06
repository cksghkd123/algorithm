N = int(input())
people_list = list(map(int, input().split()))

people_list.sort()

answer = 0
accumulate = 0
for i in range(N):
    accumulate += people_list[i]
    answer += accumulate

print(answer)