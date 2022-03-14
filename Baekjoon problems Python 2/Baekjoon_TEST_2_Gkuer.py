from itertools import combinations
import time

start = time.time()
def solution(cards):
    answer = 0

    for i in range(3,len(cards)+1):
        for card_list in list(combinations(cards,i)):
            shape_maps = {"S":0, "C":0, "D":0, "H":0}
            nums_maps = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

            for k in range(i):
                shape_maps[card_list[k][0]] += 1
                nums_maps[card_list[k][1]] += 1

            for key, value in shape_maps.items():
                if value == i:
                    answer += i**2
                    break

            for key, value in nums_maps.items():
                if value == i:
                    answer += i**2
                    break

            for key, value in shape_maps.items():
                if value > 1:
                    break
            else:
                for key, value in nums_maps.items():
                    if value > 1:
                        break
                else:
                    answer += i**2

    return answer

print(solution(["S1","D3","S3","S4","H3","H1"]))
print(solution(["C8","H8","C7","C0","D8","S8"]))
print(solution(["H1","H2","C9"]))
print(solution(["S0","C9","D7","H5"]))
print(solution(["S4","H3","H1","S1","D3","S3","S4","H3","H1","S1","D3","S3","S4","H3","H1"]))

print(time.time()-start)