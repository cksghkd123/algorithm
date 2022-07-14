from collections import defaultdict


n = int(input())

overlap_count = [[defaultdict(int) for _ in range(10)] for _ in range(n)]

for i in range(10):
    overlap_count[0][i][(i,i)] += 1


for digit_place in range(n-1):
    for number in range(10):
        for min_d, max_d in overlap_count[digit_place][number].keys():
            if 0 <= number-1:
                if number-1 < min_d:
                    overlap_count[digit_place+1][number-1][( number-1, max_d)] += overlap_count[digit_place][number][(min_d,max_d)]
                else:
                    overlap_count[digit_place+1][number-1][(min_d, max_d)] += overlap_count[digit_place][number][(min_d,max_d)]
            if number+1 < 10:
                if number+1 > max_d:
                    overlap_count[digit_place+1][number+1][(min_d, number+1)] += overlap_count[digit_place][number][(min_d,max_d)]
                else:
                    overlap_count[digit_place+1][number+1][(min_d, max_d)] += overlap_count[digit_place][number][(min_d,max_d)]

answer = 0
for i in range(1,10):
    answer += overlap_count[n-1][i][(0,9)]

answer %= 1000000000
print(answer)