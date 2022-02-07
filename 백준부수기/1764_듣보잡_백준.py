n, m = map(int,input().split())
never_heard = set()
never_seen = set()

for _ in range(n):
    never_heard.add(input())
for _ in range(m):
    never_seen.add(input())

never_hs = never_heard & never_seen
never_hs = sorted(list(never_hs))

print(len(never_hs))
for name in never_hs:
    print(name)