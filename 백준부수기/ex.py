k = {i:i for i in range(5)}
for i in range(5):
    print(k[i])

print("@@@@")

for i in k:
    print(k[i])

print("@@@@")

for i, j in k.items():
    print(i, j)
    