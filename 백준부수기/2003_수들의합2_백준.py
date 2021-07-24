n, m = map(int,input().split())
seq = list(map(int,input().split()))

answer = 0
for start in range(len(seq)):
    hap = 0
    for end in range(start,len(seq)):
        hap += seq[end]
        if hap < m:
            continue
        elif hap == m:
            answer += 1
        break

print(answer)