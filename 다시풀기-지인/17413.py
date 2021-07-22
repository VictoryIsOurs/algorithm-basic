import sys
input = sys.stdin.readline

st = []
S = input().strip()
tag = False

for s in S:
    st.append(s)
    if s == '<':
        tag = True
        tmp = ''
        st.pop()
        while st:
            tmp += st.pop()
        print(tmp, end='')
        st.append(s)
    elif s == '>':
        tmp = ''
        while st:
            tmp += st.pop()
        print(tmp[::-1], end='')
        tag = False
    elif s == ' ' and not tag:
        st.pop()
        tmp = ''
        while st:
            tmp += st.pop()
        print(tmp, end=' ')
tmp = ''
while st:
    tmp += st.pop()
print(tmp)