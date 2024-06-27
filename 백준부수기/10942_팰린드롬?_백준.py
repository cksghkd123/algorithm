import sys
input = sys.stdin.readline

N = int(input())
number_list = [0] + list(map(int, input().split()))
M = int(input())

is_palindrome = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    is_palindrome[i][i] = 1  # 길이 1인 문자열은 모두 팰린드롬

for i in range(1, N):
    if number_list[i] == number_list[i + 1]:
        is_palindrome[i][i + 1] = 1  # 길이 2인 문자열이 팰린드롬인지 체크

for string_length in range(3, N+1):
    for i in range(1, N+1-string_length+1):
        j = i + string_length -1
        if number_list[i] == number_list[j] and is_palindrome[i + 1][j - 1]:
            is_palindrome[i][j] = 1


for _ in range(M):
    S, E = map(int, input().split())
    answer = is_palindrome[S][E]
    print(answer)
