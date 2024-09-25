import collections


number_count = {1: 2, 
                2: 5,
                3: 5,
                4: 4,
                5: 5,
                6: 6,
                7: 3,
                8: 7,
                9: 6,
                0: 6}

T = int(input())

for _ in range(T):
    N = int(input())

    dp_min = {i: float('inf') for i in range(N+1)}
    dp_min[N] = 0
    dp_max = {i: 0 for i in range(N+1)}

    
    for match_count in range(N, -1, -1):

        for n, c in number_count.items():
            if match_count - c >= 0 and dp_max[match_count - c] < dp_max[match_count]*10 + n:
                dp_max[match_count - c] = dp_max[match_count]*10 + n
            
            if match_count - c >= 0 and dp_min[match_count - c] > dp_min[match_count]*10 + n and dp_min[match_count]*10 + n != 0:
                dp_min[match_count - c] = dp_min[match_count]*10 + n

    print(dp_min[0], dp_max[0])
