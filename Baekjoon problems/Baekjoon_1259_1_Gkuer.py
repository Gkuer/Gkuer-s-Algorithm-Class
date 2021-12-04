while True:
    a = input()
    if a == "0":
        break
    else:
        if a == ''.join(reversed(a)):
            print("yes")
        else:
            print("no")

# Pass