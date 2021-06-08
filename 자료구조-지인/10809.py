import sys
input = sys.stdin.readline

S = list(input().strip())
ans = [-1] * (ord('z')-ord('a')+1)

for i in range(len(S)):
    if ans[ord(S[i])-ord('a')] == -1:
        ans[ord(S[i]) - ord('a')] = i
print(*ans)