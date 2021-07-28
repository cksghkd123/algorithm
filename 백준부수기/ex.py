abc = [[1,2,3],[4,5,6],[7,8,9]]


for c in range(len(abc)):
    print(sum(map(lambda r: abc[r][c],range(3))))