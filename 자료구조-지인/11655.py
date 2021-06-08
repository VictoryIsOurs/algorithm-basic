import sys
input = sys.stdin.readline

S = input()
ans = ''
for s in S:
    if ord(s) >= ord('A') and ord(s) <= ord('Z'):
        if ord(s) + 13 > ord('Z'):
            ans += chr(ord(s) + 13 - 26)
        else:
            ans += chr(ord(s) + 13)
    elif ord(s) >= ord('a') and ord(s) <= ord('z'):
        if ord(s) + 13 > ord('z'):
            ans += chr(ord(s) + 13 - 26)
        else:
            ans += chr(ord(s) + 13)
    else:
        ans += s
print(ans)