# 1번 ~ N번
# K번째 사람을 제거
# N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람이 제거되는 순서 : (N, K)-요세푸스 순열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = [i for i in range(1, n+1)]
ans = []
cnt = 0
'''
1 2 3 4 5 6 7
'''
for i in range(len(q)):
    if 