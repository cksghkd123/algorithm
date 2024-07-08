def solution(reference, track):
    answer = 0
    n = len(reference)
    m = len(track)

    subset = set()

    for i in range(n):
        word = ''
        for j in range(i, n):
            word += reference[j]
            subset.add(word)

    dp = [0 for _ in range(m)]
    word = ''
    for i in range(n):
        if i >= m:
            break
        word += track[i]
        if word in subset:
            dp[i] = len(word)

    for i in range(1, m):
        word = ''
        for j in range(n):
            if i+j >= m:
                break
            word += track[i+j]
            if word in subset:
                dp[i+j] = max(dp[i+j], min(dp[i-1], j+1))

    answer = dp[-1]
    return answer


solution("abc", "bcab")
solution("vxrvip", "xrviprvipvxrv")