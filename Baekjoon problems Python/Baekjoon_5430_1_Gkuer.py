import sys
from collections import deque
input = sys.stdin.readline

def find():
    global n
    deq_maps = deque(maps)
    flag = False # False: 정방향 / True: 역방향
    for command in query:
        if command == "R":
            if not flag:
               flag = True
            else:
                flag = False
        else:
            if n:
                if not flag:
                    deq_maps.popleft()
                else:
                    deq_maps.pop()
                n -= 1
            else:
                return "error"
    if flag:
        return list(reversed(deq_maps))
    else:
        return list(deq_maps)

t = int(input())
for tc in range(t):
    query = input().strip()
    n = int(input())
    if n:
        maps = list(map(int,input().strip()[1:-1].split(",")))
    else:
        input()
        maps = []

    res = find()
    if res == "error":
        print(res)
    else:
        print("[",end="")
        for i in range(len(res)):
            if i != len(res)-1:
                print(res[i],end=",")
            else:
                print(res[i],end="")
        print("]")

# Pass