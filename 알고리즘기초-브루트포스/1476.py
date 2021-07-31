# E S M

#첫째 줄에 E S M으로 표시되는 가장 빠른 연도를 출력한다.
# 1 1 1은 항상 1이기 때문에, 정답이 음수가 나오는 경우는 없다.
# 15 x 28 x 19⇒ 7980 개의 조합 얼마 안되니까 그냥 다 해보면 된다 (브루트포스)

E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
year = 0

for i in range(15*28*19): #bruteForce부분
    
    year +=1
    
    if e == E and s == S and m == M: #입력받은 날들이 싹 다 같으면 
        print(year)
        break

    e+=1
    s+=1
    m+=1

    if e == 16: e = 1
    if s == 29: s = 1
    if m == 20: m = 1
