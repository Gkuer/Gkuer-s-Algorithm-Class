import sys
input = sys.stdin.readline

def do_cal(queue):
    result = queue[0]
    for i in range(0,len(queue)-2,2):
        post = queue[i+2]
        result = cal(result, post, queue[i+1])
    return result

def cal(pre, post, op):
    if op == "+":
        result = pre+post
    elif op == "-":
        result = pre-post
    else:
        result = pre * post
    return result

def insert_bracket(pointer, will_cal):
    if pointer == n-1:
        no_br = will_cal + [maps[pointer]]
        return do_cal(no_br)
    if pointer == n-3:
        no_br = will_cal + [maps[pointer], maps[pointer+1]]

        temp = cal(maps[pointer], maps[pointer+2], maps[pointer+1])
        br = will_cal + [temp]

        return max(insert_bracket(pointer+2, no_br), do_cal(br))
    # No bracket
    no_br = will_cal + [maps[pointer],maps[pointer+1]]

    # On bracket
    temp = cal(maps[pointer], maps[pointer+2], maps[pointer+1])
    br = will_cal + [temp, maps[pointer+3]]

    return max(insert_bracket(pointer+2, no_br), insert_bracket(pointer+4, br))

n = int(input())
maps = [int(x) if x != "+" and x != "-" and x != "*" else x for x in input().strip()]

print(insert_bracket(0, []))

# Success