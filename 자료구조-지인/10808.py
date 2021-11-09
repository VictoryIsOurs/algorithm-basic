import sys
input = sys.stdin.readline

S = list(input().strip())
ans = [0]*(ord('z')-ord('a')+1)

for i in range(len(S)):
    ans[ord(S[i])-ord('a')] += 1
print(*ans)