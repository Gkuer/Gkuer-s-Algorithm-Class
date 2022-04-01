text = list(input().strip())
temps = ["U","C","P","C"]

temp = 0
for i in temps:
    for j in range(len(text[temp:])):
        if text[temp+j] == i:
            temp += j+1
            break
    else:
        print("I hate UCPC")
        break
else:
    print("I love UCPC")

# Pass
