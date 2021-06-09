import sys
input = sys.stdin.readline

S = input().strip()
S_list = []
for i in range(len(S)):
    S_list.append(S[i:])
S_list = sorted(S_list)
for s in S_list:
    print(s)