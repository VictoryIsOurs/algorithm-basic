import sys
input = sys.stdin.readline

S = input().strip()
ans = ''
st = []
for s in S:
    if s.isalpha():
        ans += s
    else:
        if s == '(':
            st.append(s)
        elif s == ')':
            while st[-1] != '(':
                ans += st.pop()
            st.pop()
        elif s == '*' or s == '/':
            while st and (st[-1] == '*' or st[-1] == '/'): # 우선순위가 낮은 연산자가 나올 때까지
                ans += st.pop()
            st.append(s)
        else:
            while st and st[-1] != '(':
                ans += st.pop()
            st.append(s)
while st:
    ans += st.pop()
print(ans)
