maps = []
for i in range(1,10):
    maps.append([i,int(input())])

maps = sorted(maps,key= lambda x: x[1], reverse=True)
print(maps[0][1])
print(maps[0][0])

# Pass