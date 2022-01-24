n, m = map(int,input().split())
pokedex = {}

for i in range(1,n+1):
    pokemon = input()
    pokedex[pokemon] = i
    pokedex[str(i)] = pokemon

for _ in range(m):
    print(pokedex[input()])
