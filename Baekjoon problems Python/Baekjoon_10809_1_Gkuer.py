s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphabet)):
    if alphabet[i] in s:
        print(s.index(alphabet[i]),end=" ")
    else:
        print("-1", end=" ")

# Pass