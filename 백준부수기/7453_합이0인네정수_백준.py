import collections


n = int(input())
abcd_list = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    abcd_list.append([a, b, c, d])

first_dic = collections.defaultdict(int)
for i in range(n):
    for j in range(n):
        first_dic[abcd_list[i][0] + abcd_list[j][1]] += 1
        
answer = 0
for i in range(n):
    for j in range(n):
        answer += first_dic[-(abcd_list[i][2] + abcd_list[j][3])]


print(answer)