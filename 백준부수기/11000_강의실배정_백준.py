N = int(input())

time_sequence = []
for _ in range(N):
    s, t = map(int, input().split())
    time_sequence.append((s, 1))
    time_sequence.append((t, 0))

time_sequence.sort()
count = 0
answer = 0

for time, is_start in time_sequence:
    if is_start:
        count += 1
    else:
        count -= 1
    
    answer = max(answer, count)

print(answer)