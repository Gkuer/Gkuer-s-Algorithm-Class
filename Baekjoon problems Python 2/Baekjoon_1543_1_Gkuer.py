import sys
input = sys.stdin.readline

txt = input().strip()
kyword = input().strip()

txt = txt.replace(kyword,"_")
print(txt.count("_"))

# Pass