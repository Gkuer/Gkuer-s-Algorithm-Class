import sys
input = sys.stdin.readline

n = int(input())
maps = [int(input()) for _ in range(n)]

print(int(round(sum(maps)/n,0)))
print(sorted(maps)[len(maps)//2])

if n == 1:
    print(maps[0])
else:
    maps_dict = {}
    for i in maps:
        if i in maps_dict:
            maps_dict[i] += 1
        else:
            maps_dict[i] = 1

    maps_dict = sorted(maps_dict.items(), key=lambda x: (x[1],-x[0]), reverse=True)

    if maps_dict[0][1] == maps_dict[1][1]:
        print(maps_dict[1][0])
    else:
        print(maps_dict[0][0])


print(abs(max(maps)-min(maps)))

# Pass