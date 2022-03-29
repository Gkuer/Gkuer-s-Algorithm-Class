import sys
input = sys.stdin.readline

n = int(input())
maps = []
for _ in range(n):
    command = input().strip()
    if (command != "all") and (command != "empty"):
        command, data = command.split()
        data = int(data)
    if command == "add":
        if data not in maps:
            maps.append(data)
    elif command == "remove":
        if data in maps:
            maps.remove(data)
    elif command == "check":
        if data in maps:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if data in maps:
            maps.remove(data)
        else:
            maps.append(data)
    elif command == "all":
        maps = [i for i in range(1,21)]
    else:
        maps = []