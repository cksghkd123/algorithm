n = int(input())
conference_info = [tuple(map(int, input().split())) for _ in range(n)]

# 회의를 끝나는 시간을 기준으로 정렬
conference_info.sort(key=lambda x: (x[1], x[0]))

answer = 0
end_time = 0

for start, end in conference_info:
    if start >= end_time:
        answer += 1
        end_time = end

print(answer)
