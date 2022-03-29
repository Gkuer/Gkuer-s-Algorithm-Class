def permutation(arr,r):
    for head in range(len(arr)):
        if r == 1:
            yield [arr[head]]

        else:
            for remainder in permutation(arr[:head] + arr[head+1:], r-1):
                yield [arr[head]] + remainder

print(list(permutation([i for i in range(1,6)],3)))