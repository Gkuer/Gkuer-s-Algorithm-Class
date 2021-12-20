n = input()
maps = list(map(int,input().split()))
mx = max(maps)
ans_list = []
for i in maps:
    ans_list.append(i/mx*100)

print(sum(ans_list)/len(ans_list))

# Pass