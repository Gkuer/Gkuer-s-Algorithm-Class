import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
def get_postorder(maps):

    if len(maps) <= 1:
        return maps

    for i in range(1,len(maps)):
        if maps[0] < maps[i]:
            return get_postorder(maps[1:i]) + get_postorder(maps[i:]) + [maps[0]]

    return get_postorder(maps[1:]) + [maps[0]]

maps = []
while True:
    try:
        maps.append(int(input()))

    except:
        break


maps = get_postorder(maps)

for i in maps:
    print(i)

# Pass