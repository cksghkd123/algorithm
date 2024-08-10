N = int(input())
numbers = list(map(int, input().split()))
number_set = set(numbers)

max_number = max(numbers)
scores = [0 for _ in range(max_number+1)]

for n in numbers:
    for m in range(n, max_number+1, n):
        if m in number_set:
            scores[n] += 1
            scores[m] -= 1

for num in numbers:
    print(scores[num],end=' ')
