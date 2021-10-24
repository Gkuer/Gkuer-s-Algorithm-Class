subans = 1
for i in range(3):
    subans *= int(input())

temps = [0]*10
for x in range(10):
    for i in str(subans):
        if i == str(x):
            temps[x] += 1

for i in range(10):
    print(temps[i])

# Pass