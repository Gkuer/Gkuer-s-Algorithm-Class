import sys
input = sys.stdin.readline

n = int(input())
maps = {}


for i in range(n):
    parent, left, right = input().split()
    maps[parent] = [left,right]

def preorder(s):
    print(s,end="")
    if maps[s][0] != ".":
        preorder(maps[s][0])
    if maps[s][1] != ".":
        preorder(maps[s][1])

def inorder(s):
    if maps[s][0] != ".":
        inorder(maps[s][0])
    print(s,end="")
    if maps[s][1] != ".":
        inorder(maps[s][1])

def postorder(s):

    if maps[s][0] != ".":
        postorder(maps[s][0])
    if maps[s][1] != ".":
        postorder(maps[s][1])
    print(s, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")

# Pass