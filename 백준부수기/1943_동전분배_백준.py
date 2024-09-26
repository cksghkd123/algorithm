for _ in range(3):
    N = int(input())
    total_money = 0

    moneys = []
    for _ in range(N):
        currency, count = map(int, input().split())
        total_money += currency * count

        moneys.append((currency, count))
    
    if total_money%2 != 0:
        print(0)
        continue
    
    target = total_money // 2
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    
    for currency, count in moneys:
        for j in range(target, currency - 1, -1):
            if dp[j - currency]:
                for k in range(count):
                    if j + k * currency <= target:
                        dp[j + k * currency] = 1
                    else:
                        break

    print(dp[target])
    