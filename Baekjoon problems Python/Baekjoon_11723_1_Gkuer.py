import sys
input = sys.stdin.readline

m = int(input())
maps = [0]*21
for _ in range(m):
    data = input().strip()
    if "all" not in data and "empty" not in data:
        data, val = data.split()
        val = int(val)
        if data == "add":
            if not maps[val]:
                maps[val] = 1
        elif data == "remove":
            if maps[val]:
                maps[val] = 0
        elif data == "check":
            print(maps[val])
        elif data == "toggle":
            if maps[val]:
                maps[val] = 0
            else:
                maps[val] = 1
    else:
        if data == "all":
            for i in range(1,21):
                maps[i] = 1
        else:
            for i in range(1,21):
                maps[i] = 0

# Pass