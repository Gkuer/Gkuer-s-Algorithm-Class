import sys
import copy
input = sys.stdin.readline

def check(temps):
    temp = copy.deepcopy(temps)

    while temp:
        a = temp.pop(0)
        if a == '(':
            if not temp:
                return False
            else:
                b = temp.pop(0)
                if b != ')':
                    return False
        elif a == ')':
            return False

    return True

def cal():
    sublist = []
    x = 0
    for i in range(n):
        if maps[i] in [str(i) for i in range(10)]:
            if temps[x] == '(':
                sublist.append(temps[x])
                sublist.append(maps[i])
            elif temps[x] == '':
                sublist.append(maps[i])
            else:
                sublist.append(maps[i])
                sublist.append(temps[x])
            x += 1
        else:
            sublist.append(maps[i])
    return sublist

def cal2(tank):
    stack = []
    while tank:
        a = tank.pop(0)
        if a == '(':
            stack2 = []
            b = tank.pop(0)
            while b != ')':
                stack2.append(b)
                b = tank.pop(0)

            c = stack2.pop(0)
            while stack2:
                d = stack2.pop(0)
                e = stack2.pop(0)
                c = str(eval(c+d+e))
            stack.append(c)

        else:
            stack.append(a)

    a = stack.pop(0)
    while stack:
        b = stack.pop(0)
        c = stack.pop(0)
        a = str(eval(a+b+c))
    return int(a)

def BF(idx):
    global cnt, temps, ans
    if cnt == temps_num:
        if check(temps):
            tank = cal()
            ans = max(ans, cal2(tank))
        return

    for i in range(idx, temps_num):
        if temps[i] == "X":
            for x in range(3):
                temps[i] = cup[x]
                cnt += 1
                BF(idx+1)
                temps[i] = "X"
                cnt -= 1


n = int(input())
maps = input()
temps_num = (n + 1) // 2
temps = ["X"] * temps_num
cup = ["(", ")", ""]
cnt = 0
ans = -sys.maxsize
BF(0)
print(ans)

# Fail: Time over