import sys
input = sys.stdin.readline

n, m = map(int,input().split())
pokemon_dict = {}
for i in range(1,n+1):
    data = input().strip()
    pokemon_dict[data] = i
    pokemon_dict[str(i)] = data

for i in range(m):
    query = input().strip()
    print(pokemon_dict[query])

# Pass