import collections


def solution(words, queries):
    answer = []
    memo = {}
    for query in queries:
        if query in memo:
            answer.append(memo[query])
            continue

        count = 0
        for word in words:
            if len(word) != len(query):
                continue
            for i in range(len(query)):
                if query[i] == '?':
                    continue
                if query[i] != word[i]:
                    break
            else:
                count += 1
        memo[query] = count
        answer.append(count)

    return answer





print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))