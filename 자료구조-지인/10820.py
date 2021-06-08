import sys
input = sys.stdin.readline

while True:
    lower, upper, num, space = 0, 0, 0, 0
    arr = input().strip('\n')

    if not arr:
        break
    for a in arr:
        if a.islower():
            lower += 1
        elif a.isupper():
            upper += 1
        elif a.isdigit():
            num += 1
        else:
            space += 1
    print(lower, upper, num, space)