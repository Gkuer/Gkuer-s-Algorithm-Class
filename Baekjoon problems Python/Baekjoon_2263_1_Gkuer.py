import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    parent = postorder[post_end]
    print(parent, end=" ")

    left_length = maps[parent] - in_start
    right_length = in_end - maps[parent]

    get_preorder(in_start, in_start+left_length-1, post_start, post_start+left_length-1)
    get_preorder(in_end-right_length+1, in_end, post_end-right_length, post_end-1)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

maps = [0] * (n+1)
for i in range(n):
    maps[inorder[i]] = i

get_preorder(0, n-1, 0, n-1)

# Pass
