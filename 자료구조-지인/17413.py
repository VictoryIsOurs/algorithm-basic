### 나의 풀이 -> 나 왜이렇게 복잡하게 풀었지ㅎㅎㅎ
import sys
input = sys.stdin.readline

s = input().strip('\n')
s_list = []
ans = ""
# 1. 태그와 단어 분리
front, back = -1, -1
for i in range(len(s)):
    if s[i] == '<':
        front = i
        if front != 0 and back != 0 and front != back+1: # 태그 두 개가 붙어 있는 경우를 고려해야 한다.
            s_list.append(s[back+1:front])
    elif s[i] == '>':
        back = i
    if front < back and front != -1:
        s_list.append(s[front:back+1])
        front = -1

# 문자열이 남아있을 경우
if back < len(s)-1:
    s_list.append(s[back + 1:len(s)])

for i in range(len(s_list)):
    if s_list[i][0] == '<':
        ans += s_list[i]
    else:
        str = s_list[i].split()
        for j in range(len(str)):
            ans += str[j][::-1] + " "
        ans = ans[:-1]
print(ans)

### 남의 풀이
'''
from sys import stdin

s = stdin.readline().rstrip()
reverse = True
answer = ''
word = ''
for c in s:
    if c == '<':
        reverse = False
        answer += word
        word = '<'
    elif c == '>':
        reverse = True
        answer += (word + '>')
        word = ''
    elif c == ' ':
        answer += (word + ' ')
        word = ''
    elif reverse:
        word = c + word
    else:
        word += c
print(answer + word)
'''