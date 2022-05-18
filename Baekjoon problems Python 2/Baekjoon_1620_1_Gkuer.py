import sys
input = sys.stdin.readline

n, m = map(int,input().split())
poke_int_dict = {}
poke_str_dict = {}

for i in range(n):
    kyword = input().strip()

    poke_int_dict[i+1] = kyword
    poke_str_dict[kyword] = i+1

for i in range(m):
    quiz = input().strip()

    try:
        quiz = int(quiz)
        print(poke_int_dict[quiz])

    except:
        print(poke_str_dict[quiz])

# Pass