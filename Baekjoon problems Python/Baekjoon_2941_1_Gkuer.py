import sys
input = sys.stdin.readline

data = input().strip()
maps = ["dz=","c=","c-","d-","lj","nj","s=","z="]

for i in maps:
    data = data.replace(i,"1")

print(len(data))

# Pass