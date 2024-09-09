import collections


def solution(w, k):
    char_dic = {}

    min_answer = float('inf')
    max_answer = -1

    for i in range(len(w)):
        c = w[i]
        if c not in char_dic:
            char_dic[c] = collections.deque([i])
        else:
            char_dic[c].append(i)
        
        if len(char_dic[c]) == k:
            min_answer = min(min_answer, char_dic[c][-1] - char_dic[c][0] + 1)
            max_answer = max(max_answer, char_dic[c][-1] - char_dic[c][0] + 1)
    
            char_dic[c].popleft()
    
    if max_answer == -1:
        return [-1]
    
    return min_answer, max_answer
            

    
T = int(input())

for _ in range(T):
    W = input()
    K = int(input())

    answer = solution(W, K)

    print(*answer)