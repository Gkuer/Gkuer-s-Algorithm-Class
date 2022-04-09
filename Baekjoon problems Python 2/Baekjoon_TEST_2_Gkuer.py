# ([i for i in range(128)] (평균) * 10) + ([i for i in range(128) (평균) * 5)
# --------------------------------------------------------------------------   === [i for i in range(128)], 15 [새로운 평균값(?)]
#                                  각 인자 나누기 15


a = [2,3,5,7]
b = [5,5,2,1]
ans = []

a_cnt = 10
b_cnt = 5

for i in range(len(a)):
    a[i] *= a_cnt

for i in range(len(b)):
    b[i] *= b_cnt

for i in range(4):
    ans.append((a[i]+b[i])/(a_cnt+b_cnt))

print(str([1,2,3,4]))
