import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    cloths_dict = {}
    for i in range(n):
        thing, type = input().split()
        if type in cloths_dict:
            cloths_dict[type].append(thing)
        else:
            cloths_dict[type] = [thing]

    ans = 1
    for key, value in cloths_dict.items():
        ans *= (len(value)+1)

    print(ans-1)

# Pass