import sys
input = sys.stdin.readline

def merge_sort(li):
    global cnt

    if len(li) <= 1:
        return li

    left = merge_sort(li[:len(li)//2])
    right = merge_sort(li[len(li)//2:])

    left_start, right_start = 0, 0
    left_len, right_len = len(left), len(right)

    res = [0] * len(li)
    res_front = 0
    sub_cnt = 0
    while left_start < left_len and right_start < right_len:
        if left[left_start] <= right[right_start]:
            res[res_front] = left[left_start]
            left_start += 1
            cnt += sub_cnt
        else:
            res[res_front] = right[right_start]
            right_start += 1
            sub_cnt += 1

        res_front += 1

    if left_start < left_len:
        for i in left[left_start:]:
            res[res_front] = i
            res_front += 1
            cnt += sub_cnt
    else:
        for i in right[right_start:]:
            res[res_front] = i
            res_front += 1

    return res

n = int(input())
maps = list(map(int,input().split()))
cnt = 0
merge_sort(maps)
print(cnt)

# Pass