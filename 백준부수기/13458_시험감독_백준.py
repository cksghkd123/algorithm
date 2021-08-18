n = int(input())
takes = list(map(int,input().split()))
b, c = map(int,input().split())
answer = 0
for room in takes:
    room -= b
    answer += 1
    if room > 0:
        plus = room // c
        answer += plus
        if room % c > 0:
            answer += 1

print(answer)