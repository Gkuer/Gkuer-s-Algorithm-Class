import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n, m = map(int,input().split())
    maps = list(map(int,input().split()))

    cnt = 0
    while maps:
        flag = False
        a = maps.pop(0)
        for i in maps:
            if i > a:
                flag = True
                maps.append(a)
                break
        else:
            cnt += 1

        if not flag and m == 0:
            break
        elif flag and m == 0:
            m = len(maps)-1
        else:
            m -= 1

    print(cnt)

# Pass