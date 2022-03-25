def solution(total_sp, skills):
    def recur(pos, ini):
        if temps[pos]:
            return temps[pos]
        if maps.get(pos):
            for i in maps[pos]:
                temps[pos] += recur(i, ini)
        else:
            temps[pos] = ini
            return temps[pos]

    mx = len(skills) + 1
    maps = {}
    temps = []
    # 여기 추가
    # Root를 한번에 찾기 위해 True Array 선언    isRootArr = [True for i in range(mx+1)]
    for a, b in skills:
        temps.append(a)
        # 여기 추가
        # skills 배열에서 등장하지 않는 원소는 없다.
        # skills 배열에서 두번째로 등장하지 않는 원소가 Root가 된다.
        # isRootArr[b] = False        if a not in maps:
        maps[a] = [b]
    else:
        maps[a].append(b)


    # 여기 추가
    # skills 내부배열에서 두번째 원소로로 등장하지 않았던 원소가 Root    root = isRootArr.index(True,1)

    # 여기 제거
    # Find Root
    # for i in temps:
    #    for j in maps:
    #       if i in maps[j]:
    #           break
    #    else:    #
    #    root = i    #
    #    break
    # Find Relation Cnt
    # temps = [0 for i in range(mx+1)]
    sm = recur(root, 1)
    # Find Inition value    init_val = total_sp // sum(temps)
    # Refactor maps    for i in range(mx+1):
    temps[i] = init_val * temps[i]
    answer = temps[1:]
    return answer
