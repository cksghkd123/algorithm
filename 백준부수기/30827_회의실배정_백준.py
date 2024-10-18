import heapq

def solution(N, A):
    math_score = []
    english_score = []

    visited = [False for _ in range(N)]

    for i in range(N):
        math_score.append((-A[i][0], i))
        english_score.append((-A[i][1], i))

    math_score.sort()
    english_score.sort()

    answer = []
    count = 0

    for i in range(N):
        m_score, m_i = math_score[i]
        e_score, e_i = english_score[i]

        visited


        


n = 7
a = [[60, 70], [55, 79], [60, 80], [99, 1], [1, 99], [70, 70], [65, 75]]
answer = solution(n, a)
print(answer)