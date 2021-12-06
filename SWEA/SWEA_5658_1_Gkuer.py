import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1,t+1):
    n, k = map(int,input().split())
    maps = input().strip()
    ans_list = set()
    for i in range(n//4):
        for x in range(4):
            res = maps[(n//4)*x+i:(n//4)*(x+1)+i]
            if len(res) == n//4:
                ans_list.add(res)
            else:
                ans_list.add(res+maps[:i])

    ans_list = list(ans_list)
    print("#"+str(tc)+ " " + str(int(sorted(ans_list,key=lambda x: int(x,16),reverse=True)[k-1],16)))

# Pass