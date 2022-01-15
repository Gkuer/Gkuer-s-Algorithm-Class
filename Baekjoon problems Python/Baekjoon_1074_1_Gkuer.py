import sys
input = sys.stdin.readline

def find(idx,idy,x):
    global res
    if x == 1:
       for i in range(idx, idx+2):
           for j in range(idy, idy+2):
               res += 1
               if i == r and j == c:
                   return 1
       return 0

    else:
        a = find(idx, idy, x-1)
        if not a:
            b = find(idx, idy + 2**(x-1), x-1)
            if not b:
                d = find(idx + 2**(x-1), idy, x-1)
                if not d:
                    e = find(idx + 2**(x-1), idy + 2**(x-1), x-1)

        if a or b or d or e:
            return 1

    return 0

n, r, c = map(int,input().split())
res = -1
find(0,0,n)
print(res)

# Fail: Time Overw