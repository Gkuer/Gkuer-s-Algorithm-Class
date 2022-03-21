import time
from itertools import combinations
start = time.time()
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
combinations([i for i in range(250)], 3)
print("1. {}".format(time.time()-start))
start = time.time()
def combination(arr,r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    answer = []
    def generate(chosen):
        if len(chosen) == r:
            answer.append(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0

    generate([])

combination([i for i in range(250)], 3)

print("1. {}".format(time.time()-start))

start = time.time()
def gen_combinations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in gen_combinations(rest_arr, n-1):
            result.append([elem]+C)

    return result

gen_combinations([i for i in range(250)], 3)
print("2. {}".format(time.time() - start))

start = time.time()
lst = gen_combinations([i for i in range(250)], 3)
print("3. {}".format(time.time() - start))

start = time.time()

def combinations2(arr, r):
    global temps2
    l = len(arr)
    temps = [0 for _ in range(l)]
    temps2 = []

    def go(k,cnt):
        global temps2
        if cnt >= r:
            temp = []
            for i in range(l):
                if temps[i]:
                    temp.append(arr[i])
            temps2.append(temp)
            return

        for i in range(k,l):
            if not temps[i]:
                temps[i] = 1
                go(i+1, cnt+1)
                temps[i] = 0

    go(0,0)

combinations2([i for i in range(250)], 3)
print("4. {}".format(time.time() - start))

combination