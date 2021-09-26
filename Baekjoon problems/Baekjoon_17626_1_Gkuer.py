import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    mlist = [m*i for i in range(1,2000)]
    for i in range(1,2000):
        if n*i in mlist:
            mx_ans = n*i
            break
    nlist = []
    for i in range(1,n+1):
        if n % i == 0:
            if i not in nlist:
                nlist.append(i)
                nlist.append(n//i)
    nlist = sorted(nlist)
    for i in range(len(nlist)-1,-1,-1):
        if m % nlist[i] == 0:
            mn_ans = nlist[i]
            break
    print(mx_ans, mn_ans)